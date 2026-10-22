"""Unit tests for scripts/check_deps.py. Run: python3 -m unittest discover tests"""
import contextlib
import io
import json
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import check_deps as cd  # noqa: E402

TODAY = date(2026, 10, 22)
HEAD = ("## Register\n\n| " + " | ".join(cd.REG_COLS) + " |\n|" + "---|" * len(cd.REG_COLS) + "\n")


def issue(n, ms="M1", start="2026-11-02", target="2026-11-03", assignees=("simon",),
          blocked_by=(), updated="2026-10-21", state="OPEN", **fields):
    f = {"Start date": start, "Target date": target, "Role": fields.pop("role", "Engineer")}
    names = {"Dependency_type": "Dependency type", "Need_by": "Need-by"}
    f.update({names.get(k, k): v for k, v in fields.items()})
    return {"number": n, "title": f"Issue {n}", "state": state, "url": "", "updated": updated,
            "milestone": ms, "assignees": list(assignees), "blocked_by": list(blocked_by), "fields": f}


def row(rid, dep, blk, level="issue", label="Proposed", **cells):
    c = {"ID": rid, "Dependent": dep, "Blocker or Provider": blk, "Level": level, "Type": "Code",
         "Label": label, "Source": "test", "Status": "Open"}
    c.update(cells)
    return "| " + " | ".join(c.get(k, "") for k in cd.REG_COLS) + " |"


def run(issues, rows, milestones=None, today=TODAY):
    ms = milestones or [{"title": "M1", "due": "2026-11-30"}, {"title": "M2", "due": "2026-12-31"}]
    p = cd.load({"milestones": ms, "issues": issues}, HEAD + "\n".join(rows))
    return cd.run_checks(p, today)


def checks(concerns):
    return {(c.severity, c.check) for c in concerns}


class EdgeChecks(unittest.TestCase):
    def test_blocker_ends_after_dependent_starts(self):
        cs = run([issue(1, target="2026-11-05"), issue(2, start="2026-11-04", blocked_by=[1])],
                 [row("D1", "#2", "#1")])
        self.assertIn(("High", "blocker ends after dependent starts"), checks(cs))

    def test_same_day_handoff(self):
        cs = run([issue(1, target="2026-11-04"), issue(2, start="2026-11-04", blocked_by=[1])],
                 [row("D1", "#2", "#1")])
        self.assertIn(("Medium", "same-day handoff"), checks(cs))

    def test_zero_slack_over_weekend(self):
        cs = run([issue(1, target="2026-11-06"), issue(2, start="2026-11-09", blocked_by=[1])],
                 [row("D1", "#2", "#1")])
        self.assertIn(("Low", "zero slack"), checks(cs))

    def test_one_day_slack_is_clean(self):
        cs = run([issue(1, target="2026-11-03"), issue(2, start="2026-11-05", blocked_by=[1])],
                 [row("D1", "#2", "#1")])
        self.assertEqual(cs, [])

    def test_backward_dependency(self):
        cs = run([issue(1, ms="M2", target="2026-11-03"), issue(2, ms="M1", start="2026-11-10", blocked_by=[1])],
                 [row("D1", "#2", "#1")])
        self.assertIn(("High", "backward dependency"), checks(cs))

    def test_slipped_blocker(self):
        cs = run([issue(1, target="2026-10-20"), issue(2, start="2026-11-10", blocked_by=[1])],
                 [row("D1", "#2", "#1")])
        self.assertIn(("High", "slipped blocker"), checks(cs))

    def test_closed_blocker_is_skipped(self):
        cs = run([issue(1, target="2026-10-20", state="CLOSED"), issue(2, start="2026-10-20", blocked_by=[1])],
                 [row("D1", "#2", "#1")])
        self.assertEqual(cs, [])

    def test_stale_blocker(self):
        cs = run([issue(1, target="2026-10-26", updated="2026-10-01"),
                  issue(2, start="2026-10-28", blocked_by=[1])],
                 [row("D1", "#2", "#1")])
        self.assertIn(("Medium", "stale blocker"), checks(cs))

    def test_cycle(self):
        cs = run([issue(1, blocked_by=[2]), issue(2, blocked_by=[1])],
                 [row("D1", "#2", "#1"), row("D2", "#1", "#2")])
        self.assertIn(("High", "cycle"), checks(cs))


class NodeChecks(unittest.TestCase):
    def test_milestone_overrun(self):
        cs = run([issue(1, target="2026-12-05")], [])
        self.assertIn(("High", "milestone overrun"), checks(cs))

    def test_missing_owner_is_reported_and_left_blank(self):
        cs = run([issue(1, assignees=())], [])
        c = next(c for c in cs if c.check == "missing owner or date")
        self.assertIn("owner", c.detail)

    def test_non_code_committed_missing(self):
        cs = run([issue(5, start=None, target=None, Dependency_type="Vendor", Need_by="2026-11-04")], [])
        self.assertIn(("Medium", "need-by gap"), checks(cs))
        self.assertNotIn(("Medium", "missing owner or date"), checks(cs))

    def test_non_code_committed_late(self):
        cs = run([issue(5, start=None, target=None, Dependency_type="Privacy",
                        Need_by="2026-11-04", Committed="2026-11-10")], [])
        self.assertIn(("High", "need-by gap"), checks(cs))

    def test_non_code_blocker_uses_committed(self):
        cs = run([issue(5, start=None, target=None, Dependency_type="Licensing",
                        Need_by="2026-11-04", Committed="2026-11-06"),
                  issue(2, start="2026-11-05", blocked_by=[5])],
                 [row("D1", "#2", "#5", level="external")])
        self.assertIn(("High", "blocker ends after dependent starts"), checks(cs))


class RegisterAndDrift(unittest.TestCase):
    def test_link_only_on_github(self):
        cs = run([issue(1, target="2026-11-01"), issue(2, start="2026-11-10", blocked_by=[1])], [])
        self.assertIn(("Medium", "link missing from register"), checks(cs))

    def test_row_only_in_register(self):
        cs = run([issue(1, target="2026-11-01"), issue(2, start="2026-11-10")], [row("D1", "#2", "#1")])
        self.assertIn(("Low", "register edge without GitHub link"), checks(cs))

    def test_edge_needs_leading_issue_number(self):
        r = cd.Row({"Dependent": "#25 Dockerfile", "Blocker or Provider": "Docker install (done in #25)"})
        self.assertIsNone(r.edge)

    def test_check_only_writes_nothing(self):
        with tempfile.TemporaryDirectory() as d:
            reg = Path(d) / "deps.md"
            data = Path(d) / "snap.json"
            reg.write_text(HEAD + row("D1", "#2", "#1") + "\n")
            data.write_text(json.dumps({"milestones": [{"title": "M1", "due": "2026-11-30"}],
                                        "issues": [issue(1), issue(2, blocked_by=[1])]}))
            before = reg.read_text()
            with contextlib.redirect_stdout(io.StringIO()):
                cd.main(["--data", str(data), "--register", str(reg), "--today", "2026-10-22"])
                cd.main(["--data", str(data), "--register", str(reg), "--today", "2026-10-22", "--summary"])
            self.assertEqual(reg.read_text(), before)

    def test_write_fills_concerns_and_maps(self):
        with tempfile.TemporaryDirectory() as d:
            reg = Path(d) / "deps.md"
            data = Path(d) / "snap.json"
            reg.write_text(HEAD + row("D1", "#2", "#1") + "\n")
            data.write_text(json.dumps({"milestones": [{"title": "M1", "due": "2026-11-30"}],
                                        "issues": [issue(1, target="2026-11-04"),
                                                   issue(2, start="2026-11-04", blocked_by=[1])]}))
            with contextlib.redirect_stdout(io.StringIO()):
                cd.main(["--data", str(data), "--register", str(reg), "--today", "2026-10-22", "--write"])
            text = reg.read_text()
            self.assertIn("| D1 | #2 | #1 |", text)
            self.assertIn("| C1 |", text)
            # program, one per milestone (M1), across milestones, component, role, external
            self.assertEqual(text.count("```mermaid"), 6)
            self.assertIn(cd.GEN_BEGIN, text)


if __name__ == "__main__":
    unittest.main()
