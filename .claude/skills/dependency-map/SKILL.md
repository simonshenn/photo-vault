---
name: dependency-map
description: Discover, check, and map Photo Vault dependencies (issue, component, role, and non-code such as legal, privacy, licensing, vendor, cost approvals). Use for the weekly status Dependencies section, when issues or design docs change, or when asked about blockers, slack, or dependency risk. Check-only by default; every link, date, and register change needs Simon's approval.
---

# dependency-map

Keeps `docs/program/dependencies.md` (register and five maps) and GitHub
Blocked by links in line with the program, and reports date concerns.

## Modes

| Mode | When | Writes |
|---|---|---|
| Check-only (default) | Weekly status, GitHub workflow, any question about dependencies | Nothing |
| Propose | Simon asks to update dependencies, or check-only finds drift | Nothing until Simon approves each item |
| Apply | After approval | One change per tool call |

Check-only commands:

```
python3 scripts/check_deps.py            # full concern report
python3 scripts/check_deps.py --summary  # Dependencies section for the weekly status
```

In check-only mode, run only these commands and read-only `gh` calls. Never
run `gh issue edit`, `gh issue create`, `gh project item-edit`, or file edits.

## Discover

Sources, in this order: open issues and their bodies, `docs/program/raid.md`,
`docs/design.md` and `docs/requirements.md`, `docs/program/charter.md`, then
the code (imports, workflow files, Dockerfile) once it exists.

Levels to cover:
- **Issue:** one issue needs another finished first.
- **Component:** a module, workflow, image, or secret needs another.
- **Role:** derived from issue links where the two issues have different Role values. Add no rows for this level.
- **External and non-code:** legal, privacy, licensing, vendor, cost approval, tooling. State "none identified" with the date checked when a category has nothing.

Label every candidate:
- **Proposed:** a recorded source states it. Cite the file or issue and quote the phrase.
- **Inferred:** your reasoning with no recorded statement. Give the reasoning as the source. Owner is "owner missing" until Simon names one. Never fill an owner, Need-by, or Committed date from reasoning alone.

## Propose

Present one table for approval with, for each item: register row (all
columns), GitHub change (`gh issue edit <dependent> --add-blocked-by <blocker>`),
and for non-code items a new issue with Dependency type, Provider, Need-by,
and Committed on Project 1. Need-by is the earliest start date among its
dependents. Leave Committed blank when no source gives it.

## Apply (after approval)

- Links: `gh issue edit <dependent> -R simonshenn/photo-vault --add-blocked-by <n>[,<n>]`, one call per dependent issue.
- Non-code issues: create, set milestone (the one containing Need-by), add to Project 1, set fields. One call per issue.
- Register: edit the Register table in `docs/program/dependencies.md`, then run `python3 scripts/check_deps.py --write` to refresh the Concerns column and the generated maps. Commit as its own call.

Fallback if Blocked by links become unavailable: a `Blocked by: #N` line in the
issue body and a "Blocked by" text field on Project 1.

## Report concerns

Use the script output. For each concern give: issue links, the dates compared,
severity, suggested action, and who verifies (roles). Group Low zero-slack
items into chains in prose. Lead with High, then Medium.

## Weekly status

Paste `--summary` output as the Dependencies section of
`docs/program/status/YYYY-MM-DD.md`. Add one line per High concern with the
decision needed and its owner.

## Rules

- Follow CLAUDE.md Planning rules and Simon's writing style.
- The repo is public. Keep concern reports in the job summary or local output; post nothing to issue comments.
- Surface gaps (owner missing, Committed missing, stale data) as concerns; never fill them in.
