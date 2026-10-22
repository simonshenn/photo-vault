#!/usr/bin/env python3
"""Dependency checks and maps for Photo Vault.

Reads issues, Blocked by links, and Project 1 fields from GitHub (through `gh`),
joins them with the register in docs/program/dependencies.md, and reports
date concerns. Standard library only; runs on Python 3.9+.

Modes:
  (default)    check-only report in Markdown. Writes nothing.
  --summary    short Dependencies section for the weekly status. Writes nothing.
  --write      regenerate the Concerns column and the generated section of
               dependencies.md. Run only after Simon approves the change.

Use --data <file> to run against a saved snapshot instead of GitHub.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import date, timedelta
from pathlib import Path

OWNER, REPO, PROJECT = "simonshenn", "photo-vault", 1
ROOT = Path(__file__).resolve().parent.parent
REGISTER = ROOT / "docs" / "program" / "dependencies.md"
GEN_BEGIN = "<!-- BEGIN GENERATED: scripts/check_deps.py --write -->"
GEN_END = "<!-- END GENERATED -->"
REG_COLS = ["ID", "Dependent", "Blocker or Provider", "Level", "Type", "Label",
            "Source", "Need-by", "Committed", "Owner", "Status", "Concerns"]
SEVERITIES = ("High", "Medium", "Low")
STALE_DAYS, STALE_WINDOW = 14, 7

QUERY = """
query($owner: String!, $repo: String!) {
  repository(owner: $owner, name: $repo) {
    milestones(first: 50, states: [OPEN, CLOSED]) { nodes { title dueOn state } }
    issues(first: 100, states: [OPEN, CLOSED]) { nodes {
      number title state updatedAt url
      milestone { title }
      assignees(first: 5) { nodes { login } }
      blockedBy(first: 50) { nodes { number } }
      projectItems(first: 10) { nodes {
        project { number }
        fieldValues(first: 30) { nodes {
          ... on ProjectV2ItemFieldDateValue { date field { ... on ProjectV2FieldCommon { name } } }
          ... on ProjectV2ItemFieldSingleSelectValue { name field { ... on ProjectV2FieldCommon { name } } }
          ... on ProjectV2ItemFieldNumberValue { number field { ... on ProjectV2FieldCommon { name } } }
          ... on ProjectV2ItemFieldTextValue { text field { ... on ProjectV2FieldCommon { name } } }
        } }
      } }
    } }
  }
}
"""


# ---------------------------------------------------------------- data model

@dataclass
class Issue:
    number: int
    title: str
    state: str
    url: str
    updated: date
    milestone: str | None
    assignees: list[str]
    blocked_by: list[int]
    fields: dict[str, object]

    def d(self, name: str) -> date | None:
        v = self.fields.get(name)
        return date.fromisoformat(v) if isinstance(v, str) and v else None

    @property
    def start(self) -> date | None:
        return self.d("Start date")

    @property
    def target(self) -> date | None:
        return self.d("Target date")

    @property
    def role(self) -> str | None:
        return self.fields.get("Role")  # type: ignore[return-value]

    @property
    def dep_type(self) -> str:
        return self.fields.get("Dependency type") or "Code"  # type: ignore[return-value]

    @property
    def non_code(self) -> bool:
        return self.dep_type != "Code"

    @property
    def is_open(self) -> bool:
        return self.state == "OPEN"


@dataclass
class Row:
    cells: dict[str, str]

    def __getitem__(self, k: str) -> str:
        return self.cells.get(k, "")

    def refs(self, col: str) -> list[int]:
        return [int(n) for n in re.findall(r"#(\d+)", self[col])]

    @property
    def edge(self) -> tuple[int, int] | None:
        """Issue link, only when both cells start with an issue number."""
        dep = re.match(r"#(\d+)", self["Dependent"])
        blk = re.match(r"#(\d+)", self["Blocker or Provider"])
        return (int(dep[1]), int(blk[1])) if dep and blk else None

    @property
    def inferred(self) -> bool:
        return self["Label"].strip().lower() == "inferred"


@dataclass
class Concern:
    severity: str
    check: str
    detail: str
    action: str
    verify: str
    edge: tuple[int, int] | None = None
    node: int | None = None
    id: str = ""
    rows: list[str] = field(default_factory=list)

    @property
    def issues(self) -> list[int]:
        return list(self.edge) if self.edge else [self.node] if self.node else []


@dataclass
class Program:
    issues: dict[int, Issue]
    due: dict[str, date | None]      # milestone title -> due date
    rows: list[Row]

    def order(self) -> list[str]:
        """Milestones by due date; ones without a due date (M0) first."""
        return sorted(self.due, key=lambda t: (self.due[t] or date.min, t))

    def ms_index(self, title: str | None) -> int:
        order = self.order()
        return order.index(title) if title in order else -1


# ---------------------------------------------------------------- loading

def fetch_snapshot() -> dict:
    out = subprocess.run(
        ["gh", "api", "graphql", "-f", f"query={QUERY}", "-F", f"owner={OWNER}", "-F", f"repo={REPO}"],
        check=True, capture_output=True, text=True).stdout
    repo = json.loads(out)["data"]["repository"]
    issues = []
    for n in repo["issues"]["nodes"]:
        fields: dict[str, object] = {}
        for item in n["projectItems"]["nodes"]:
            if item["project"]["number"] != PROJECT:
                continue
            for fv in item["fieldValues"]["nodes"]:
                if not fv or "field" not in fv:
                    continue
                value = next((fv[k] for k in ("date", "name", "number", "text") if k in fv), None)
                fields[fv["field"]["name"]] = value
        issues.append({
            "number": n["number"], "title": n["title"], "state": n["state"], "url": n["url"],
            "updated": n["updatedAt"][:10],
            "milestone": (n["milestone"] or {}).get("title"),
            "assignees": [a["login"] for a in n["assignees"]["nodes"]],
            "blocked_by": [b["number"] for b in n["blockedBy"]["nodes"]],
            "fields": fields,
        })
    milestones = [{"title": m["title"], "due": (m["dueOn"] or "")[:10] or None}
                  for m in repo["milestones"]["nodes"]]
    return {"milestones": milestones, "issues": issues}


def parse_register(text: str) -> list[Row]:
    rows, in_reg = [], False
    for line in text.splitlines():
        if line.startswith("## "):
            in_reg = line.strip() == "## Register"
            continue
        if not in_reg or not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells[0] in ("ID", "") or set(cells[0]) <= {"-", ":"}:
            continue
        rows.append(Row(dict(zip(REG_COLS, cells))))
    return rows


def load(snapshot: dict, register_text: str) -> Program:
    issues = {}
    for i in snapshot["issues"]:
        issues[i["number"]] = Issue(
            number=i["number"], title=i["title"], state=i["state"], url=i.get("url", ""),
            updated=date.fromisoformat(i["updated"]), milestone=i.get("milestone"),
            assignees=i.get("assignees", []), blocked_by=i.get("blocked_by", []),
            fields=i.get("fields", {}))
    due = {m["title"]: date.fromisoformat(m["due"]) if m.get("due") else None
           for m in snapshot["milestones"]}
    return Program(issues, due, parse_register(register_text))


# ---------------------------------------------------------------- checks

def workdays_between(a: date, b: date) -> int:
    """Working days strictly between a and b."""
    n, x = 0, a + timedelta(days=1)
    while x < b:
        n += x.weekday() < 5
        x += timedelta(days=1)
    return n


def blocker_end(p: Program, blk: Issue, row: Row | None) -> date | None:
    """When a blocker is done: Committed for non-code dependencies, Target for issues."""
    if blk.non_code:
        if blk.d("Committed"):
            return blk.d("Committed")
        if row and re.match(r"\d{4}-\d{2}-\d{2}$", row["Committed"]):
            return date.fromisoformat(row["Committed"])
        return None
    return blk.target


def verifiers(*issues: Issue) -> str:
    roles = []
    for i in issues:
        r = i.role or ("owner missing" if not i.assignees else None)
        if r and r not in roles:
            roles.append(r)
    return ", ".join(roles) or "TPM"


def run_checks(p: Program, today: date) -> list[Concern]:
    out: list[Concern] = []
    edges: dict[tuple[int, int], Row | None] = {}
    for r in p.rows:
        if r.edge and all(n in p.issues for n in r.edge):
            edges.setdefault(r.edge, r)

    for (dn, bn), row in edges.items():
        dep, blk = p.issues[dn], p.issues[bn]
        tag = f" ({row['Label']})" if row else ""
        if p.ms_index(blk.milestone) > p.ms_index(dep.milestone):
            out.append(Concern("High", "backward dependency",
                               f"#{bn} in {blk.milestone}, #{dn} in {dep.milestone}",
                               f"Move #{bn} to an earlier milestone or #{dn} to a later one",
                               verifiers(blk, dep), edge=(dn, bn)))
        if not blk.is_open:
            continue
        end = blocker_end(p, blk, row)
        start = dep.start or (dep.d("Need-by") if dep.non_code else None)
        if end and start:
            if end > start:
                out.append(Concern("High", "blocker ends after dependent starts",
                                   f"#{bn} {'committed' if blk.non_code else 'target'} {end} > #{dn} start {start}{tag}",
                                   f"Move #{dn} start after {end}, or split #{dn}",
                                   verifiers(blk, dep), edge=(dn, bn)))
            elif end == start:
                out.append(Concern("Medium", "same-day handoff",
                                   f"#{bn} target {end} = #{dn} start {start}{tag}",
                                   f"Accept if the handoff happens in order that day, or move #{dn} start one working day",
                                   verifiers(blk, dep), edge=(dn, bn)))
            elif workdays_between(end, start) == 0:
                out.append(Concern("Low", "zero slack",
                                   f"#{bn} target {end}, #{dn} start {start}{tag}",
                                   "Accept as planned and watch in the weekly status",
                                   verifiers(blk, dep), edge=(dn, bn)))
        if end and end < today:
            out.append(Concern("High", "slipped blocker",
                               f"#{bn} still open, {'committed' if blk.non_code else 'target'} {end} < today {today}",
                               f"Update #{bn} dates or status, then re-check #{dn}",
                               verifiers(blk, dep), edge=(dn, bn)))
        if start and (start - today).days <= STALE_WINDOW and (today - blk.updated).days > STALE_DAYS:
            out.append(Concern("Medium", "stale blocker",
                               f"#{bn} last updated {blk.updated}, #{dn} starts {start}",
                               f"Ask the owner of #{bn} for a status update",
                               verifiers(blk, dep), edge=(dn, bn)))

    for n, i in sorted(p.issues.items()):
        if not i.is_open:
            continue
        due = p.due.get(i.milestone or "")
        if due and i.target and i.target > due:
            out.append(Concern("High", "milestone overrun", f"#{n} target {i.target} > {i.milestone} due {due}",
                               f"Move #{n} target inside {i.milestone} or re-propose the milestone date",
                               verifiers(i), node=n))
        if i.non_code:
            need, committed = i.d("Need-by"), i.d("Committed")
            if not i.assignees:
                out.append(Concern("Medium", "missing owner", f"#{n} {i.dep_type}: owner missing",
                                   f"Confirm an owner for #{n}", "TPM", node=n))
            if not need:
                out.append(Concern("Medium", "missing date", f"#{n} Need-by missing",
                                   f"Set Need-by on #{n} from its earliest dependent", "TPM", node=n))
            elif not committed:
                out.append(Concern("Medium", "need-by gap", f"#{n} Need-by {need}, Committed missing",
                                   f"Set a Committed date on #{n} on or before {need}",
                                   verifiers(i), node=n))
            elif committed > need:
                out.append(Concern("High", "need-by gap", f"#{n} Committed {committed} > Need-by {need}",
                                   f"Pull #{n} Committed before {need}, or move its dependents",
                                   verifiers(i), node=n))
        else:
            missing = [k for k, v in (("owner", i.assignees), ("start", i.start), ("target", i.target)) if not v]
            if missing:
                out.append(Concern("Medium", "missing owner or date", f"#{n} missing {', '.join(missing)}",
                                   f"Set {', '.join(missing)} on #{n}", verifiers(i), node=n))

    # drift between the register and GitHub Blocked by links
    reg = set(edges)
    gh = {(n, b) for n, i in p.issues.items() for b in i.blocked_by}
    for dn, bn in sorted(gh - reg):
        out.append(Concern("Medium", "link missing from register", f"#{dn} blocked by #{bn} on GitHub only",
                           "Add a register row with its source, or remove the link", "TPM", edge=(dn, bn)))
    for dn, bn in sorted(reg - gh):
        out.append(Concern("Low", "register edge without GitHub link", f"#{dn} after #{bn} in register only",
                           "Add the Blocked by link after approval, or remove the row", "TPM", edge=(dn, bn)))

    out.extend(find_cycles(reg | gh))

    out.sort(key=lambda c: (SEVERITIES.index(c.severity), c.check, c.issues))
    for k, c in enumerate(out, 1):
        c.id = f"C{k}"
        c.rows = [r["ID"] for r in p.rows
                  if (c.edge and r.edge == c.edge)
                  or (c.node and c.node in r.refs("Dependent") + r.refs("Blocker or Provider"))]
    return out


def find_cycles(edges: set[tuple[int, int]]) -> list[Concern]:
    graph: dict[int, list[int]] = {}
    for d, b in edges:
        graph.setdefault(d, []).append(b)
    out, done, path = [], set(), []

    def visit(n: int) -> None:
        if n in path:
            loop = path[path.index(n):] + [n]
            out.append(Concern("High", "cycle", " -> ".join(f"#{x}" for x in loop),
                               "Remove one link in the cycle; slack checks skip these issues",
                               "TPM", node=n))
            return
        if n in done:
            return
        path.append(n)
        for m in sorted(graph.get(n, [])):
            visit(m)
        path.pop()
        done.add(n)

    for n in sorted(graph):
        visit(n)
    return out


# ---------------------------------------------------------------- output

def link(p: Program, n: int) -> str:
    i = p.issues.get(n)
    return f"[#{n}]({i.url})" if i and i.url else f"#{n}"


def report(p: Program, concerns: list[Concern]) -> str:
    lines = ["| ID | Severity | Check | Issues | Dates compared | Suggested action | Verify | Register rows |",
             "|---|---|---|---|---|---|---|---|"]
    for c in concerns:
        lines.append(f"| {c.id} | {c.severity} | {c.check} | {', '.join(link(p, n) for n in c.issues)} | "
                     f"{c.detail} | {c.action} | {c.verify} | {', '.join(c.rows)} |")
    counts = {s: sum(c.severity == s for c in concerns) for s in SEVERITIES}
    head = f"High {counts['High']} · Medium {counts['Medium']} · Low {counts['Low']}"
    return head + "\n\n" + ("\n".join(lines) if concerns else "No concerns.")


def summary(p: Program, concerns: list[Concern]) -> str:
    counts = {s: sum(c.severity == s for c in concerns) for s in SEVERITIES}
    lines = ["## Dependencies", "",
             f"High {counts['High']} · Medium {counts['Medium']} · Low {counts['Low']}. "
             f"Source: scripts/check_deps.py, register docs/program/dependencies.md.", ""]
    for c in concerns:
        if c.severity != "Low":
            lines.append(f"- {c.id} {c.severity}, {c.check}: {', '.join(link(p, n) for n in c.issues)}. "
                         f"{c.detail}. Action: {c.action}. Verify: {c.verify}.")
    return "\n".join(lines)


# ---------------------------------------------------------------- maps

CLASSDEFS = ["  classDef high fill:#fde2e1,stroke:#c62828,stroke-width:2px",
             "  classDef med fill:#fff4ce,stroke:#b7791f,stroke-width:2px",
             "  classDef done fill:#e6f4ea,stroke:#2e7d32",
             "  classDef inferred stroke-dasharray:5 5"]


def md(d: date | None) -> str:
    return d.strftime("%m-%d") if d else "?"


def esc(s: str) -> str:
    return s.replace('"', "#quot;")


class Marks:
    """Concern lookup by node and edge, for highlighting."""

    def __init__(self, concerns: list[Concern]):
        self.node: dict[int, list[Concern]] = {}
        self.edge: dict[tuple[int, int], list[Concern]] = {}
        for c in concerns:
            if c.edge:
                self.edge.setdefault(c.edge, []).append(c)
                self.node.setdefault(c.edge[0], []).append(c)
            elif c.node:
                self.node.setdefault(c.node, []).append(c)

    @staticmethod
    def worst(cs: list[Concern]) -> str | None:
        sev = [c.severity for c in cs if c.severity != "Low"]
        return "high" if "High" in sev else "med" if sev else None

    @staticmethod
    def ids(cs: list[Concern]) -> str:
        return " ".join(c.id for c in cs if c.severity != "Low")


def issue_label(p: Program, i: Issue, inferred: set[int], short: bool = False) -> str:
    title = i.title if len(i.title) <= 38 else i.title[:36] + "…"
    if i.non_code:
        when = f"need-by {md(i.d('Need-by'))} · committed {md(i.d('Committed')) if i.d('Committed') else 'missing'}"
    else:
        when = f"{md(i.start)}→{md(i.target)}"
    owner = "<br/>owner missing" if not i.assignees else ""
    label = f"#{i.number} {i.milestone.split()[0] if short and i.milestone else title}<br/>{when}{owner}"
    return esc(label)


def node_class(p: Program, i: Issue, marks: Marks, inferred: set[int]) -> list[str]:
    cls = []
    if not i.is_open:
        cls.append("done")
    w = marks.worst(marks.node.get(i.number, []))
    if w:
        cls.append(w)
    if i.number in inferred or (i.non_code and not i.assignees):
        cls.append("inferred")
    return cls


def edge_line(row: Row | None, a: str, b: str, cs: list[Concern]) -> str:
    ids = Marks.ids(cs)
    label = ids or ("0 slack" if any(c.check == "zero slack" for c in cs) else "")
    if row and row.inferred:
        label = (label + " Inferred").strip()
    arrow = ("-. " + f'"{label}"' + " .->") if row and row.inferred and label else \
            ("-.->" if row and row.inferred else (f'-- "{label}" -->' if label else "-->"))
    return f"  {a} {arrow} {b}"


def render(lines: list[str], classes: dict[str, list[str]], link_styles: list[str] = ()) -> str:
    out = ["```mermaid", "flowchart LR", *CLASSDEFS, *lines]
    for cls in ("done", "high", "med", "inferred"):
        ids = [n for n, cs in classes.items() if cls in cs]
        if ids:
            out.append(f"  class {','.join(ids)} {cls}")
    out.extend(link_styles)
    out.append("```")
    return "\n".join(out)


def issue_edges(p: Program) -> dict[tuple[int, int], Row]:
    out = {}
    for r in p.rows:
        if r.edge and all(n in p.issues for n in r.edge):
            out.setdefault(r.edge, r)
    return out


def inferred_nodes(p: Program) -> set[int]:
    """Non-code issues whose register rows are all Inferred."""
    by_blk: dict[int, list[Row]] = {}
    for r in p.rows:
        for n in r.refs("Blocker or Provider"):
            by_blk.setdefault(n, []).append(r)
    return {n for n, rs in by_blk.items()
            if n in p.issues and p.issues[n].non_code and all(r.inferred for r in rs)}


def map_program(p: Program, marks: Marks) -> str:
    order = p.order()
    lines, classes = [], {}
    for k, t in enumerate(order):
        members = [i for i in p.issues.values() if i.milestone == t]
        cs = [c for i in members for c in marks.node.get(i.number, []) if c.edge is None or c.edge[0] == i.number]
        open_n = sum(i.is_open for i in members)
        state = "done" if members and open_n == 0 else f"{open_n} open"
        ids = Marks.ids(cs)
        due = f"due {md(p.due[t])}" if p.due[t] else "no due date"
        lines.append(f'  M{k}["{esc(t)}<br/>{due} · {state}' + (f"<br/>{ids}" if ids else "") + '"]')
        classes[f"M{k}"] = ["done"] if state == "done" else [w for w in [Marks.worst(cs)] if w]
        if k:
            lines.append(f"  M{k - 1} --> M{k}")
    return render(lines, classes)


def map_issue(p: Program, marks: Marks, milestone: str | None) -> str:
    edges, inferred = issue_edges(p), inferred_nodes(p)
    lines, classes, used = [], {}, set()
    if milestone is None:   # edges across milestones
        pairs = [(e, r) for e, r in edges.items()
                 if p.issues[e[0]].milestone != p.issues[e[1]].milestone]
        for (d, b), _ in pairs:
            used.update((d, b))
    else:
        pairs = [(e, r) for e, r in edges.items()
                 if p.issues[e[0]].milestone == milestone == p.issues[e[1]].milestone]
        used = {n for n, i in p.issues.items() if i.milestone == milestone}
    for n in sorted(used):
        i = p.issues[n]
        lines.append(f'  i{n}["{issue_label(p, i, inferred, short=False)}"]')
        classes[f"i{n}"] = node_class(p, i, marks, inferred)
    for (d, b), r in sorted(pairs):
        lines.append(edge_line(r, f"i{b}", f"i{d}", marks.edge.get((d, b), [])))
    return render(lines, classes)


def map_component(p: Program, marks: Marks) -> str:
    ids: dict[str, str] = {}
    lines, classes = [], {}

    def nid(name: str) -> str:
        if name not in ids:
            ids[name] = f"c{len(ids)}"
            cs = [c for n in map(int, re.findall(r"#(\d+)", name)) for c in marks.node.get(n, [])]
            extra = Marks.ids(cs)
            lines.append(f'  {ids[name]}["{esc(name)}' + (f"<br/>{extra}" if extra else "") + '"]')
            classes[ids[name]] = [w for w in [Marks.worst(cs)] if w]
        return ids[name]

    for r in p.rows:
        if r["Level"] != "component":
            continue
        a, b = nid(r["Blocker or Provider"]), nid(r["Dependent"])
        lines.append(f"  {a} {'-.->' if r.inferred else '-->'} {b}")
    return render(lines, classes)


def map_roles(p: Program, marks: Marks) -> str:
    agg: dict[tuple[str, str], list[tuple[tuple[int, int], Row]]] = {}
    for (d, b), r in issue_edges(p).items():
        rb, rd = p.issues[b].role, p.issues[d].role
        if rb and rd and rb != rd:
            agg.setdefault((rb, rd), []).append(((d, b), r))
    roles = sorted({x for k in agg for x in k})
    rid = {name: f"r{k}" for k, name in enumerate(roles)}
    lines = [f'  {rid[name]}["{esc(name)}"]' for name in roles]
    styles = []
    for k, ((rb, rd), items) in enumerate(sorted(agg.items())):
        cs = [c for e, _ in items for c in marks.edge.get(e, [])]
        pairs = ", ".join(f"#{b}→#{d}" for (d, b), _ in sorted(items))
        label = esc(pairs + (" " + Marks.ids(cs) if Marks.ids(cs) else ""))
        dashed = all(r.inferred for _, r in items)
        lines.append(f'  {rid[rb]} -' + ('. "' + label + '" .->' if dashed else '- "' + label + '" -->') + f" {rid[rd]}")
        w = Marks.worst(cs)
        if w:
            color = "#c62828" if w == "high" else "#b7791f"
            styles.append(f"  linkStyle {k} stroke:{color},stroke-width:2px")
    return render(lines, {}, styles)


def map_external(p: Program, marks: Marks) -> str:
    lines, classes, seen = [], {}, set()
    inferred = inferred_nodes(p)
    for k, r in enumerate(x for x in p.rows if x["Level"] == "external"):
        lead = re.match(r"#(\d+)", r["Blocker or Provider"])
        blk_refs, dep_refs = ([int(lead[1])] if lead else []), r.refs("Dependent")
        if blk_refs and blk_refs[0] in p.issues:
            bi = p.issues[blk_refs[0]]
            bid = f"i{bi.number}"
            owner = ", ".join(bi.assignees) or "missing"
            need = bi.d("Need-by") or (date.fromisoformat(r["Need-by"]) if re.match(r"\d{4}-", r["Need-by"]) else None)
            committed = bi.d("Committed") if bi.non_code else bi.target
            kind = " · ".join(x for x in (r["Type"], bi.fields.get("Provider")) if x)
            label = (f"{r['Blocker or Provider']}<br/>{kind}<br/>"
                     f"owner {owner} · need-by {md(need)} · committed {md(committed) if committed else 'missing'}")
            cls = node_class(p, bi, marks, inferred)
        else:
            bid = f"x{k}"
            label = (f"{r['Blocker or Provider']}<br/>{r['Type']}<br/>owner {r['Owner'] or 'owner missing'} · "
                     f"need-by {r['Need-by'] or '?'} · committed {r['Committed'] or 'missing'}")
            cls = ["inferred"] if r.inferred else []
        cs = [c for n in blk_refs for c in marks.node.get(n, []) if c.edge is None]
        if Marks.ids(cs):
            label += f"<br/>{Marks.ids(cs)}"
        if bid not in seen:
            lines.append(f'  {bid}["{esc(label)}"]')
            classes[bid] = cls
            seen.add(bid)
        for d in dep_refs:
            if d in p.issues and f"i{d}" not in seen:
                lines.append(f'  i{d}["{issue_label(p, p.issues[d], inferred)}"]')
                classes[f"i{d}"] = node_class(p, p.issues[d], marks, inferred)
                seen.add(f"i{d}")
            edge_cs = marks.edge.get((d, blk_refs[0]), []) if blk_refs else []
            lines.append(edge_line(r, bid, f"i{d}", edge_cs))
    return render(lines, classes)


def generated_section(p: Program, concerns: list[Concern], today: date) -> str:
    order = p.order()
    marks = Marks(concerns)
    parts = [GEN_BEGIN, "", f"Generated {today} from the register and Project 1.", "",
             "## Concerns", "", report(p, concerns), "",
             "## Maps", "",
             "Arrows point from the blocker to the dependent. Dashed: Inferred. "
             "Red: High concern. Amber: Medium concern. Green: done. Dates: start→target.", "",
             "### Level 1: Program", "", map_program(p, marks), "",
             "### Level 2: Issues", ""]
    for t in order:
        parts += [f"#### {t}", "", map_issue(p, marks, t), ""]
    parts += ["#### Across milestones", "", map_issue(p, marks, None), "",
              "### Level 3: Components", "", map_component(p, marks), "",
              "### Level 4: Role handoffs", "", map_roles(p, marks), "",
              "### Level 5: External and non-code", "", map_external(p, marks), "", GEN_END]
    return "\n".join(parts)


def write_register(text: str, p: Program, concerns: list[Concern], today: date) -> str:
    by_row: dict[str, list[str]] = {}
    for c in concerns:
        for rid in c.rows:
            by_row.setdefault(rid, []).append(c.id)
    out, in_reg = [], False
    for line in text.splitlines():
        if line.startswith("## "):
            in_reg = line.strip() == "## Register"
        if in_reg and line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if cells[0] not in ("ID", "") and not set(cells[0]) <= {"-", ":"}:
                cells += [""] * (len(REG_COLS) - len(cells))
                cells[REG_COLS.index("Concerns")] = " ".join(by_row.get(cells[0], []))
                line = "| " + " | ".join(cells) + " |"
        out.append(line)
    text = "\n".join(out) + "\n"
    gen = generated_section(p, concerns, today)
    if GEN_BEGIN in text:
        head, rest = text.split(GEN_BEGIN, 1)
        tail = rest.split(GEN_END, 1)[1] if GEN_END in rest else ""
        return head + gen + tail
    return text.rstrip("\n") + "\n\n" + gen + "\n"


# ---------------------------------------------------------------- main

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", type=Path, help="snapshot JSON to use instead of GitHub")
    ap.add_argument("--register", type=Path, default=REGISTER)
    ap.add_argument("--today", type=date.fromisoformat, default=date.today())
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--summary", action="store_true", help="Dependencies section for the weekly status")
    mode.add_argument("--write", action="store_true", help="update dependencies.md (needs approval)")
    args = ap.parse_args(argv)

    snapshot = json.loads(args.data.read_text()) if args.data else fetch_snapshot()
    text = args.register.read_text()
    p = load(snapshot, text)
    concerns = run_checks(p, args.today)

    if args.write:
        args.register.write_text(write_register(text, p, concerns, args.today))
        print(f"Updated {args.register} ({len(concerns)} concerns)")
    elif args.summary:
        print(summary(p, concerns))
    else:
        print(report(p, concerns))
    return 0


if __name__ == "__main__":
    sys.exit(main())
