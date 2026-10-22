# Dependencies: Photo Vault

Register of dependencies at issue, component, role, and external level, with
date concerns and five maps. Owner: Simon (TPM). Maintained with the
`dependency-map` skill and `scripts/check_deps.py`.

- **Label.** Proposed: a recorded source states it. Inferred: Claude's
  reasoning, owner missing until Simon confirms one.
- **Direction.** Dependent needs Blocker or Provider. Issue rows mirror GitHub
  Blocked by links.
- **Dates.** Issue start and target dates come from Project 1. Need-by and
  Committed come from Project 1 for non-code issues, or from this table for
  rows without an issue.
- **Changes.** Rows, links, and dates change only after Simon approves.
  `check_deps.py --write` updates the Concerns column and the generated
  section below.
- **Legal.** None identified (personal, non-commercial project; checked
  2026-10-22).

## Register

| ID | Dependent | Blocker or Provider | Level | Type | Label | Source | Need-by | Committed | Owner | Status | Concerns |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DEP-001 | #2 Review intent PR | #1 intent.md | issue | Code | Proposed | #2 body "Closes #1"; date plan 2026-10-21 |  |  | board | Open | C13 |
| DEP-002 | #5 requirements.md | #2 Review intent PR | issue | Code | Proposed | Date plan 2026-10-21 |  |  | board | Open |  |
| DEP-003 | #6 design.md | #5 requirements.md | issue | Code | Proposed | Date plan 2026-10-21 |  |  | board | Open | C14 |
| DEP-004 | #6 design.md | #8 HEIC test run (R1) | external | Tooling | Proposed | Date plan 2026-10-21; raid.md R1 | 2026-11-04 |  | board | Open | C15 |
| DEP-005 | #7 Threat list | #6 design.md | issue | Code | Proposed | Date plan 2026-10-21 |  |  | board | Open | C16 |
| DEP-006 | #9 Design review | #7 Threat list | issue | Code | Proposed | Date plan 2026-10-21 |  |  | board | Open | C17 |
| DEP-007 | #13 CLAUDE.md and skill | #10 Skeleton | issue | Code | Proposed | Date plan 2026-10-21 (M3 order change) |  |  | board | Open | C21 |
| DEP-008 | #11 Login | #10 Skeleton | issue | Code | Proposed | Date plan 2026-10-21 |  |  | board | Open |  |
| DEP-009 | #11 Login | #13 CLAUDE.md and skill | issue | Code | Proposed | Date plan 2026-10-21 |  |  | board | Open | C19 |
| DEP-010 | #12 Upload and gallery | #11 Login | issue | Code | Proposed | Date plan 2026-10-21 |  |  | board | Open | C20 |
| DEP-011 | #14 Worktrees | #12 Upload and gallery | issue | Code | Proposed | Date plan 2026-10-21 |  |  | board | Open | C10 |
| DEP-012 | #17 Hook | #14 Worktrees | issue | Code | Proposed | Date plan 2026-10-21 ("M3 tests already exist") |  |  | board | Open | C23 |
| DEP-013 | #16 pytest suite | #17 Hook | issue | Code | Proposed | Date plan 2026-10-21 |  |  | board | Open | C22 |
| DEP-014 | #19 Evals | #18 Weekly-status skill | issue | Code | Proposed | Date plan 2026-10-21 |  |  | board | Open | C24 |
| DEP-015 | #20 evals.yml | #19 Evals | issue | Code | Proposed | Date plan 2026-10-21 |  |  | board | Open | C25 |
| DEP-016 | #23 Claude review | #22 CI | issue | Code | Proposed | Date plan 2026-10-21 |  |  | board | Open | C26 |
| DEP-017 | #26 deploy.yml | #25 Dockerfile | issue | Code | Proposed | Date plan 2026-10-21 |  |  | board | Open | C27 |
| DEP-018 | #27 Launch checklist | #26 deploy.yml | issue | Code | Proposed | Date plan 2026-10-21; C1 split approved 2026-10-22 |  |  | board | Open | C11 |
| DEP-019 | #29 Metrics scripts | #28 Middleware | issue | Code | Proposed | Date plan 2026-10-21 |  |  | board | Open | C28 |
| DEP-020 | #30 Metrics review | #29 Metrics scripts | issue | Code | Proposed | Date plan 2026-10-21 |  |  | board | Open | C29 |
| DEP-021 | #31 Retro | #30 Metrics review | issue | Code | Proposed | Date plan 2026-10-21 |  |  | board | Open | C12 |
| DEP-022 | #8 HEIC test run | #3 Python 3.12 (D2) | external | Tooling | Inferred | #8 needs python:3.12; #3 installs it | 2026-11-03 |  | board | Open |  |
| DEP-023 | #10 Skeleton | #3 Python 3.12 (D2) | external | Tooling | Proposed | raid.md D2 "Blocks M3" | 2026-11-09 |  | board | Open |  |
| DEP-024 | #10 Skeleton | #9 Design review | issue | Code | Inferred | Build starts after the design merge |  |  | board | Open | C18 |
| DEP-025 | #19 Evals | #13 CLAUDE.md and skill | issue | Code | Inferred | The add-route eval needs the skill |  |  | board | Open |  |
| DEP-026 | #22 CI | #16 pytest suite | issue | Code | Inferred | ci.yml runs the pytest suite |  |  | board | Open |  |
| DEP-027 | #23 Claude review | #20 evals.yml and key | issue | Code | Inferred | Claude review needs the ANTHROPIC_API_KEY secret from #20 |  |  | board | Open |  |
| DEP-028 | #25 Dockerfile | #8 HEIC test run | issue | Code | Inferred | The Dockerfile relies on the pillow-heif result |  |  | board | Open |  |
| DEP-029 | #26 deploy.yml | #22 CI | issue | Code | Inferred | Deploy runs after CI checks |  |  | board | Open |  |
| DEP-030 | #28 Middleware | #12 Upload and gallery | issue | Code | Inferred | The middleware wraps app routes |  |  | board | Open |  |
| DEP-031 | #18 Weekly-status skill | #36 dependency-map skill | issue | Code | Proposed | Dependency-map proposal approved 2026-10-22 (status feed) |  |  | board | Open |  |
| DEP-032 | #19 Evals | #36 dependency-map skill | issue | Code | Proposed | Dependency-map proposal approved 2026-10-22 (eval cases) |  |  | board | Open |  |
| DEP-033 | #22 CI | #36 dependency-map skill | issue | Code | Proposed | Dependency-map proposal approved 2026-10-22 (deps-check.yml) |  |  | board | Open |  |
| DEP-034 | #25 Dockerfile | Docker Desktop install (D3, done in #25) | external | Tooling | Proposed | raid.md D3 | 2026-12-14 | in #25 | Simon | Open |  |
| DEP-035 | #20 evals.yml | #38 API key and spending limit (D4) | external | Cost approval | Proposed | raid.md D4 | 2026-12-04 |  | board | Open | C5 |
| DEP-036 | #23 Claude review | #38 API key and spending limit (D4) | external | Cost approval | Proposed | raid.md D4 | 2026-12-09 |  | board | Open | C5 |
| DEP-037 | #12 Upload and gallery | #39 pillow-heif licenses (N1) | external | Licensing | Inferred | First pass 2026-10-22 | 2026-11-16 |  | owner missing | Open | C1 C6 |
| DEP-038 | #26 deploy.yml | #39 pillow-heif licenses (N1) | external | Licensing | Inferred | First pass 2026-10-22 (public GHCR image) | 2026-12-16 |  | owner missing | Open | C1 C6 |
| DEP-039 | #6 design.md | #40 EXIF and GPS metadata (N2) | external | Privacy | Inferred | First pass 2026-10-22 | 2026-11-04 |  | owner missing | Open | C2 C7 |
| DEP-040 | #22 CI | #41 read:project token (N3) | external | Vendor | Inferred | Dependency-map design 2026-10-22 | 2026-12-07 |  | owner missing | Open | C3 C8 |
| DEP-041 | #25 Dockerfile | #42 Docker Desktop license (N4) | external | Vendor | Inferred | First pass 2026-10-22 | 2026-12-14 |  | owner missing | Open | C4 C9 |
| DEP-042 | app/main.py | app/db.py | component | Component | Proposed | #10 body |  |  |  | Planned |  |
| DEP-043 | app/main.py | templates/ | component | Component | Proposed | #10 body |  |  |  | Planned |  |
| DEP-044 | app/main.py | app/auth.py | component | Component | Proposed | #11 body "Every photo route requires a session" |  |  |  | Planned |  |
| DEP-045 | app/main.py | app/photos.py | component | Component | Proposed | #12 body |  |  |  | Planned |  |
| DEP-046 | app/photos.py | app/auth.py | component | Component | Proposed | #11 body |  |  |  | Planned |  |
| DEP-047 | app/photos.py | app/db.py | component | Component | Proposed | #12 body "record in SQLite" |  |  |  | Planned |  |
| DEP-048 | app/photos.py | storage/ (gitignored) | component | Component | Proposed | #12 body |  |  |  | Planned |  |
| DEP-049 | app/photos.py | pillow-heif (#39) | component | Licensing | Proposed | #8, #12 bodies |  |  |  | Planned | C1 C6 |
| DEP-050 | tests/ | app/main.py | component | Component | Proposed | #16 body |  |  |  | Planned |  |
| DEP-051 | .claude hook: ruff, pytest | tests/ | component | Component | Proposed | #17 body |  |  |  | Planned |  |
| DEP-052 | ci.yml | tests/ | component | Component | Proposed | #22 body |  |  |  | Planned |  |
| DEP-053 | evals.yml | evals/ | component | Component | Proposed | #20 body |  |  |  | Planned |  |
| DEP-054 | evals.yml | ANTHROPIC_API_KEY (#38) | component | Cost approval | Proposed | #20 body |  |  |  | Planned | C5 |
| DEP-055 | Claude review workflow | ANTHROPIC_API_KEY (#38) | component | Cost approval | Inferred | #23 uses the key from #20 |  |  |  | Planned | C5 |
| DEP-056 | deps-check.yml | scripts/check_deps.py | component | Component | Proposed | #22 body |  |  |  | Planned |  |
| DEP-057 | deps-check.yml | read:project token (#41) | component | Vendor | Proposed | #22 body |  |  |  | Planned | C3 C8 |
| DEP-058 | scripts/check_deps.py | docs/program/dependencies.md | component | Component | Proposed | #36 body |  |  |  | Built |  |
| DEP-059 | deploy.yml | Dockerfile | component | Component | Proposed | #26 body |  |  |  | Planned |  |
| DEP-060 | Dockerfile | pillow-heif (#39) | component | Licensing | Proposed | #25 body |  |  |  | Planned | C1 C6 |
| DEP-061 | GHCR image (public) | deploy.yml | component | Component | Proposed | #26 body |  |  |  | Planned |  |
| DEP-062 | staging, production Environments | GHCR image (public) | component | Component | Proposed | #26 body |  |  |  | Planned |  |
| DEP-063 | timing middleware | app/main.py | component | Component | Inferred | #28 wraps app routes |  |  |  | Planned |  |
| DEP-064 | metrics.jsonl | timing middleware | component | Component | Proposed | #28 body |  |  |  | Planned |  |
| DEP-065 | scripts/check_metrics.py | metrics.jsonl | component | Component | Proposed | #29 body |  |  |  | Planned |  |
| DEP-066 | docs/intent/002 | scripts/check_metrics.py | component | Component | Proposed | #29 body |  |  |  | Planned |  |

<!-- BEGIN GENERATED: scripts/check_deps.py --write -->

Generated 2026-10-22 from the register and Project 1.

## Concerns

High 0 · Medium 12 · Low 17

| ID | Severity | Check | Issues | Dates compared | Suggested action | Verify | Register rows |
|---|---|---|---|---|---|---|---|
| C1 | Medium | missing owner | [#39](https://github.com/simonshenn/photo-vault/issues/39) | #39 Licensing: owner missing | Confirm an owner for #39 | TPM | DEP-037, DEP-038, DEP-049, DEP-060 |
| C2 | Medium | missing owner | [#40](https://github.com/simonshenn/photo-vault/issues/40) | #40 Privacy: owner missing | Confirm an owner for #40 | TPM | DEP-039 |
| C3 | Medium | missing owner | [#41](https://github.com/simonshenn/photo-vault/issues/41) | #41 Vendor: owner missing | Confirm an owner for #41 | TPM | DEP-040, DEP-057 |
| C4 | Medium | missing owner | [#42](https://github.com/simonshenn/photo-vault/issues/42) | #42 Vendor: owner missing | Confirm an owner for #42 | TPM | DEP-041 |
| C5 | Medium | need-by gap | [#38](https://github.com/simonshenn/photo-vault/issues/38) | #38 Need-by 2026-12-04, Committed missing | Set a Committed date on #38 on or before 2026-12-04 | TPM | DEP-035, DEP-036, DEP-054, DEP-055 |
| C6 | Medium | need-by gap | [#39](https://github.com/simonshenn/photo-vault/issues/39) | #39 Need-by 2026-11-16, Committed missing | Set a Committed date on #39 on or before 2026-11-16 | owner missing | DEP-037, DEP-038, DEP-049, DEP-060 |
| C7 | Medium | need-by gap | [#40](https://github.com/simonshenn/photo-vault/issues/40) | #40 Need-by 2026-11-04, Committed missing | Set a Committed date on #40 on or before 2026-11-04 | owner missing | DEP-039 |
| C8 | Medium | need-by gap | [#41](https://github.com/simonshenn/photo-vault/issues/41) | #41 Need-by 2026-12-07, Committed missing | Set a Committed date on #41 on or before 2026-12-07 | owner missing | DEP-040, DEP-057 |
| C9 | Medium | need-by gap | [#42](https://github.com/simonshenn/photo-vault/issues/42) | #42 Need-by 2026-12-14, Committed missing | Set a Committed date on #42 on or before 2026-12-14 | owner missing | DEP-041 |
| C10 | Medium | same-day handoff | [#14](https://github.com/simonshenn/photo-vault/issues/14), [#12](https://github.com/simonshenn/photo-vault/issues/12) | #12 target 2026-11-18 = #14 start 2026-11-18 (Proposed) | Accept if the handoff happens in order that day, or move #14 start one working day | Engineer | DEP-011 |
| C11 | Medium | same-day handoff | [#27](https://github.com/simonshenn/photo-vault/issues/27), [#26](https://github.com/simonshenn/photo-vault/issues/26) | #26 target 2026-12-17 = #27 start 2026-12-17 (Proposed) | Accept if the handoff happens in order that day, or move #27 start one working day | SRE, TPM | DEP-018 |
| C12 | Medium | same-day handoff | [#31](https://github.com/simonshenn/photo-vault/issues/31), [#30](https://github.com/simonshenn/photo-vault/issues/30) | #30 target 2027-01-07 = #31 start 2027-01-07 (Proposed) | Accept if the handoff happens in order that day, or move #31 start one working day | Product Manager, TPM | DEP-021 |
| C13 | Low | zero slack | [#2](https://github.com/simonshenn/photo-vault/issues/2), [#1](https://github.com/simonshenn/photo-vault/issues/1) | #1 target 2026-10-28, #2 start 2026-10-29 (Proposed) | Accept as planned and watch in the weekly status | Product Manager | DEP-001 |
| C14 | Low | zero slack | [#6](https://github.com/simonshenn/photo-vault/issues/6), [#5](https://github.com/simonshenn/photo-vault/issues/5) | #5 target 2026-11-03, #6 start 2026-11-04 (Proposed) | Accept as planned and watch in the weekly status | Tech Lead | DEP-003 |
| C15 | Low | zero slack | [#6](https://github.com/simonshenn/photo-vault/issues/6), [#8](https://github.com/simonshenn/photo-vault/issues/8) | #8 target 2026-11-03, #6 start 2026-11-04 (Proposed) | Accept as planned and watch in the weekly status | Engineer, Tech Lead | DEP-004 |
| C16 | Low | zero slack | [#7](https://github.com/simonshenn/photo-vault/issues/7), [#6](https://github.com/simonshenn/photo-vault/issues/6) | #6 target 2026-11-04, #7 start 2026-11-05 (Proposed) | Accept as planned and watch in the weekly status | Tech Lead, AppSec | DEP-005 |
| C17 | Low | zero slack | [#9](https://github.com/simonshenn/photo-vault/issues/9), [#7](https://github.com/simonshenn/photo-vault/issues/7) | #7 target 2026-11-05, #9 start 2026-11-06 (Proposed) | Accept as planned and watch in the weekly status | AppSec, TPM | DEP-006 |
| C18 | Low | zero slack | [#10](https://github.com/simonshenn/photo-vault/issues/10), [#9](https://github.com/simonshenn/photo-vault/issues/9) | #9 target 2026-11-06, #10 start 2026-11-09 (Inferred) | Accept as planned and watch in the weekly status | TPM, Engineer | DEP-024 |
| C19 | Low | zero slack | [#11](https://github.com/simonshenn/photo-vault/issues/11), [#13](https://github.com/simonshenn/photo-vault/issues/13) | #13 target 2026-11-11, #11 start 2026-11-12 (Proposed) | Accept as planned and watch in the weekly status | Tech Lead, Engineer | DEP-009 |
| C20 | Low | zero slack | [#12](https://github.com/simonshenn/photo-vault/issues/12), [#11](https://github.com/simonshenn/photo-vault/issues/11) | #11 target 2026-11-13, #12 start 2026-11-16 (Proposed) | Accept as planned and watch in the weekly status | Engineer | DEP-010 |
| C21 | Low | zero slack | [#13](https://github.com/simonshenn/photo-vault/issues/13), [#10](https://github.com/simonshenn/photo-vault/issues/10) | #10 target 2026-11-10, #13 start 2026-11-11 (Proposed) | Accept as planned and watch in the weekly status | Engineer, Tech Lead | DEP-007 |
| C22 | Low | zero slack | [#16](https://github.com/simonshenn/photo-vault/issues/16), [#17](https://github.com/simonshenn/photo-vault/issues/17) | #17 target 2026-11-23, #16 start 2026-11-24 (Proposed) | Accept as planned and watch in the weekly status | QA engineer | DEP-013 |
| C23 | Low | zero slack | [#17](https://github.com/simonshenn/photo-vault/issues/17), [#14](https://github.com/simonshenn/photo-vault/issues/14) | #14 target 2026-11-20, #17 start 2026-11-23 (Proposed) | Accept as planned and watch in the weekly status | Engineer, QA engineer | DEP-012 |
| C24 | Low | zero slack | [#19](https://github.com/simonshenn/photo-vault/issues/19), [#18](https://github.com/simonshenn/photo-vault/issues/18) | #18 target 2026-11-30, #19 start 2026-12-01 (Proposed) | Accept as planned and watch in the weekly status | TPM, Platform engineer | DEP-014 |
| C25 | Low | zero slack | [#20](https://github.com/simonshenn/photo-vault/issues/20), [#19](https://github.com/simonshenn/photo-vault/issues/19) | #19 target 2026-12-03, #20 start 2026-12-04 (Proposed) | Accept as planned and watch in the weekly status | Platform engineer | DEP-015 |
| C26 | Low | zero slack | [#23](https://github.com/simonshenn/photo-vault/issues/23), [#22](https://github.com/simonshenn/photo-vault/issues/22) | #22 target 2026-12-08, #23 start 2026-12-09 (Proposed) | Accept as planned and watch in the weekly status | Platform engineer, Reviewer | DEP-016 |
| C27 | Low | zero slack | [#26](https://github.com/simonshenn/photo-vault/issues/26), [#25](https://github.com/simonshenn/photo-vault/issues/25) | #25 target 2026-12-15, #26 start 2026-12-16 (Proposed) | Accept as planned and watch in the weekly status | SRE | DEP-017 |
| C28 | Low | zero slack | [#29](https://github.com/simonshenn/photo-vault/issues/29), [#28](https://github.com/simonshenn/photo-vault/issues/28) | #28 target 2027-01-04, #29 start 2027-01-05 (Proposed) | Accept as planned and watch in the weekly status | SRE | DEP-019 |
| C29 | Low | zero slack | [#30](https://github.com/simonshenn/photo-vault/issues/30), [#29](https://github.com/simonshenn/photo-vault/issues/29) | #29 target 2027-01-06, #30 start 2027-01-07 (Proposed) | Accept as planned and watch in the weekly status | SRE, Product Manager | DEP-020 |

## Maps

Arrows point from the blocker to the dependent. Dashed: Inferred. Red: High concern. Amber: Medium concern. Green: done. Dates: start→target.

### Level 1: Program

```mermaid
flowchart LR
  classDef high fill:#fde2e1,stroke:#c62828,stroke-width:2px
  classDef med fill:#fff4ce,stroke:#b7791f,stroke-width:2px
  classDef done fill:#e6f4ea,stroke:#2e7d32
  classDef inferred stroke-dasharray:5 5
  M0["M0 Setup<br/>no due date · done"]
  M1["M1 Plan<br/>due 10-30 · 5 open"]
  M0 --> M1
  M2["M2 Design<br/>due 11-06 · 6 open<br/>C2 C7"]
  M1 --> M2
  M3["M3 Build<br/>due 11-20 · 7 open<br/>C10 C1 C6"]
  M2 --> M3
  M4["M4 Test<br/>due 12-04 · 7 open<br/>C5"]
  M3 --> M4
  M5["M5 Deploy<br/>due 12-18 · 9 open<br/>C11 C3 C8 C4 C9"]
  M4 --> M5
  M6["M6 Maintain<br/>due 01-08 · 5 open<br/>C12"]
  M5 --> M6
  class M0 done
  class M2,M3,M4,M5,M6 med
```

### Level 2: Issues

#### M0 Setup

```mermaid
flowchart LR
  classDef high fill:#fde2e1,stroke:#c62828,stroke-width:2px
  classDef med fill:#fff4ce,stroke:#b7791f,stroke-width:2px
  classDef done fill:#e6f4ea,stroke:#2e7d32
  classDef inferred stroke-dasharray:5 5
  i33["#33 Repo init, .gitignore, README, chart…<br/>10-21→10-21"]
  i34["#34 Public GitHub repo, Milestones M0 to…<br/>10-21→10-21"]
  i35["#35 Milestone breakdown, estimates, date…<br/>10-21→10-21"]
  class i33,i34,i35 done
```

#### M1 Plan

```mermaid
flowchart LR
  classDef high fill:#fde2e1,stroke:#c62828,stroke-width:2px
  classDef med fill:#fff4ce,stroke:#b7791f,stroke-width:2px
  classDef done fill:#e6f4ea,stroke:#2e7d32
  classDef inferred stroke-dasharray:5 5
  i1["#1 Write intent.md for Photo Vault v1<br/>10-27→10-28"]
  i2["#2 Review intent PR with Claude and merge<br/>10-29→10-29"]
  i3["#3 Install Python 3.12 (RAID D2)<br/>10-26→10-26"]
  i4["#4 Status template and first weekly sta…<br/>10-29→10-30"]
  i36["#36 dependency-map skill: register, chec…<br/>10-22→10-27"]
  i1 -- "0 slack" --> i2
```

#### M2 Design

```mermaid
flowchart LR
  classDef high fill:#fde2e1,stroke:#c62828,stroke-width:2px
  classDef med fill:#fff4ce,stroke:#b7791f,stroke-width:2px
  classDef done fill:#e6f4ea,stroke:#2e7d32
  classDef inferred stroke-dasharray:5 5
  i5["#5 Write requirements.md from intent<br/>11-02→11-03"]
  i6["#6 Write design.md: routes, data model,…<br/>11-04→11-04"]
  i7["#7 Threat list and privacy review<br/>11-05→11-05"]
  i8["#8 HEIC test run with pillow-heif (RAID…<br/>11-03→11-03"]
  i9["#9 Design review, PR merge, weekly stat…<br/>11-06→11-06"]
  i40["#40 Dependency: EXIF and GPS metadata in…<br/>need-by 11-04 · committed missing<br/>owner missing"]
  i5 -- "0 slack" --> i6
  i8 -- "0 slack" --> i6
  i40 -. "Inferred" .-> i6
  i6 -- "0 slack" --> i7
  i7 -- "0 slack" --> i9
  class i40 med
  class i40 inferred
```

#### M3 Build

```mermaid
flowchart LR
  classDef high fill:#fde2e1,stroke:#c62828,stroke-width:2px
  classDef med fill:#fff4ce,stroke:#b7791f,stroke-width:2px
  classDef done fill:#e6f4ea,stroke:#2e7d32
  classDef inferred stroke-dasharray:5 5
  i10["#10 App skeleton in plan mode<br/>11-09→11-10"]
  i11["#11 Single-user login and sessions<br/>11-12→11-13"]
  i12["#12 Upload, storage, and gallery<br/>11-16→11-18"]
  i13["#13 CLAUDE.md via /init and add-route sk…<br/>11-11→11-11"]
  i14["#14 Parallel worktrees: thumbnails and d…<br/>11-18→11-20"]
  i15["#15 Weekly status x2 and RAID review (20…<br/>11-13→11-20"]
  i39["#39 Dependency: pillow-heif bundled code…<br/>need-by 11-16 · committed missing<br/>owner missing"]
  i10 --> i11
  i13 -- "0 slack" --> i11
  i11 -- "0 slack" --> i12
  i39 -. "Inferred" .-> i12
  i10 -- "0 slack" --> i13
  i12 -- "C10" --> i14
  class i14,i39 med
  class i39 inferred
```

#### M4 Test

```mermaid
flowchart LR
  classDef high fill:#fde2e1,stroke:#c62828,stroke-width:2px
  classDef med fill:#fff4ce,stroke:#b7791f,stroke-width:2px
  classDef done fill:#e6f4ea,stroke:#2e7d32
  classDef inferred stroke-dasharray:5 5
  i16["#16 pytest suite including 401 privacy t…<br/>11-24→11-25"]
  i17["#17 PostToolUse hook running ruff and py…<br/>11-23→11-23"]
  i18["#18 Weekly-status skill<br/>11-30→11-30"]
  i19["#19 Evals: run_evals.py with 3 tasks<br/>12-01→12-03"]
  i20["#20 evals.yml and API key secret (RAID D4)<br/>12-04→12-04"]
  i21["#21 Exit criteria and weekly status x2 (…<br/>11-23→12-04"]
  i38["#38 Dependency: Anthropic API key and sp…<br/>need-by 12-04 · committed missing"]
  i17 -- "0 slack" --> i16
  i18 -- "0 slack" --> i19
  i19 -- "0 slack" --> i20
  i38 --> i20
  class i38 med
```

#### M5 Deploy

```mermaid
flowchart LR
  classDef high fill:#fde2e1,stroke:#c62828,stroke-width:2px
  classDef med fill:#fff4ce,stroke:#b7791f,stroke-width:2px
  classDef done fill:#e6f4ea,stroke:#2e7d32
  classDef inferred stroke-dasharray:5 5
  i22["#22 ci.yml and branch protection with re…<br/>12-07→12-08"]
  i23["#23 Claude PR review, CODEOWNERS, plante…<br/>12-09→12-10"]
  i24["#24 PreToolUse approval hook<br/>12-11→12-11"]
  i25["#25 Install Docker (RAID D3) and write D…<br/>12-14→12-15"]
  i26["#26 deploy.yml, GHCR, staging and produc…<br/>12-16→12-17"]
  i27["#27 Launch checklist, go/no-go, weekly s…<br/>12-17→12-18"]
  i37["#37 Weekly status (2026-12-11)<br/>12-11→12-11"]
  i41["#41 Dependency: read:project token for t…<br/>need-by 12-07 · committed missing<br/>owner missing"]
  i42["#42 Dependency: Docker Desktop license t…<br/>need-by 12-14 · committed missing<br/>owner missing"]
  i41 -. "Inferred" .-> i22
  i22 -- "0 slack" --> i23
  i42 -. "Inferred" .-> i25
  i22 -. "Inferred" .-> i26
  i25 -- "0 slack" --> i26
  i26 -- "C11" --> i27
  class i27,i41,i42 med
  class i41,i42 inferred
```

#### M6 Maintain

```mermaid
flowchart LR
  classDef high fill:#fde2e1,stroke:#c62828,stroke-width:2px
  classDef med fill:#fff4ce,stroke:#b7791f,stroke-width:2px
  classDef done fill:#e6f4ea,stroke:#2e7d32
  classDef inferred stroke-dasharray:5 5
  i28["#28 Timing middleware writing metrics.js…<br/>01-04→01-04"]
  i29["#29 fake_metrics.py and check_metrics.py…<br/>01-05→01-06"]
  i30["#30 Metrics review and decision on inten…<br/>01-07→01-07"]
  i31["#31 Retro-001 and learning-log wrap-up<br/>01-07→01-08"]
  i32["#32 Weekly status (2027-01-08)<br/>01-08→01-08"]
  i28 -- "0 slack" --> i29
  i29 -- "0 slack" --> i30
  i30 -- "C12" --> i31
  class i31 med
```

#### Across milestones

```mermaid
flowchart LR
  classDef high fill:#fde2e1,stroke:#c62828,stroke-width:2px
  classDef med fill:#fff4ce,stroke:#b7791f,stroke-width:2px
  classDef done fill:#e6f4ea,stroke:#2e7d32
  classDef inferred stroke-dasharray:5 5
  i2["#2 Review intent PR with Claude and merge<br/>10-29→10-29"]
  i3["#3 Install Python 3.12 (RAID D2)<br/>10-26→10-26"]
  i5["#5 Write requirements.md from intent<br/>11-02→11-03"]
  i8["#8 HEIC test run with pillow-heif (RAID…<br/>11-03→11-03"]
  i9["#9 Design review, PR merge, weekly stat…<br/>11-06→11-06"]
  i10["#10 App skeleton in plan mode<br/>11-09→11-10"]
  i12["#12 Upload, storage, and gallery<br/>11-16→11-18"]
  i13["#13 CLAUDE.md via /init and add-route sk…<br/>11-11→11-11"]
  i14["#14 Parallel worktrees: thumbnails and d…<br/>11-18→11-20"]
  i16["#16 pytest suite including 401 privacy t…<br/>11-24→11-25"]
  i17["#17 PostToolUse hook running ruff and py…<br/>11-23→11-23"]
  i18["#18 Weekly-status skill<br/>11-30→11-30"]
  i19["#19 Evals: run_evals.py with 3 tasks<br/>12-01→12-03"]
  i20["#20 evals.yml and API key secret (RAID D4)<br/>12-04→12-04"]
  i22["#22 ci.yml and branch protection with re…<br/>12-07→12-08"]
  i23["#23 Claude PR review, CODEOWNERS, plante…<br/>12-09→12-10"]
  i25["#25 Install Docker (RAID D3) and write D…<br/>12-14→12-15"]
  i26["#26 deploy.yml, GHCR, staging and produc…<br/>12-16→12-17"]
  i28["#28 Timing middleware writing metrics.js…<br/>01-04→01-04"]
  i36["#36 dependency-map skill: register, chec…<br/>10-22→10-27"]
  i38["#38 Dependency: Anthropic API key and sp…<br/>need-by 12-04 · committed missing"]
  i39["#39 Dependency: pillow-heif bundled code…<br/>need-by 11-16 · committed missing<br/>owner missing"]
  i2 --> i5
  i3 -. "Inferred" .-> i8
  i3 --> i10
  i9 -. "0 slack Inferred" .-> i10
  i14 -- "0 slack" --> i17
  i36 --> i18
  i13 -. "Inferred" .-> i19
  i36 --> i19
  i16 -. "Inferred" .-> i22
  i36 --> i22
  i20 -. "Inferred" .-> i23
  i38 --> i23
  i8 -. "Inferred" .-> i25
  i39 -. "Inferred" .-> i26
  i12 -. "Inferred" .-> i28
  class i14,i38,i39 med
  class i39 inferred
```

### Level 3: Components

```mermaid
flowchart LR
  classDef high fill:#fde2e1,stroke:#c62828,stroke-width:2px
  classDef med fill:#fff4ce,stroke:#b7791f,stroke-width:2px
  classDef done fill:#e6f4ea,stroke:#2e7d32
  classDef inferred stroke-dasharray:5 5
  c0["app/db.py"]
  c1["app/main.py"]
  c0 --> c1
  c2["templates/"]
  c2 --> c1
  c3["app/auth.py"]
  c3 --> c1
  c4["app/photos.py"]
  c4 --> c1
  c3 --> c4
  c0 --> c4
  c5["storage/ (gitignored)"]
  c5 --> c4
  c6["pillow-heif (#39)<br/>C1 C6"]
  c6 --> c4
  c7["tests/"]
  c1 --> c7
  c8[".claude hook: ruff, pytest"]
  c7 --> c8
  c9["ci.yml"]
  c7 --> c9
  c10["evals/"]
  c11["evals.yml"]
  c10 --> c11
  c12["ANTHROPIC_API_KEY (#38)<br/>C5"]
  c12 --> c11
  c13["Claude review workflow"]
  c12 -.-> c13
  c14["scripts/check_deps.py"]
  c15["deps-check.yml"]
  c14 --> c15
  c16["read:project token (#41)<br/>C3 C8"]
  c16 --> c15
  c17["docs/program/dependencies.md"]
  c17 --> c14
  c18["Dockerfile"]
  c19["deploy.yml"]
  c18 --> c19
  c6 --> c18
  c20["GHCR image (public)"]
  c19 --> c20
  c21["staging, production Environments"]
  c20 --> c21
  c22["timing middleware"]
  c1 -.-> c22
  c23["metrics.jsonl"]
  c22 --> c23
  c24["scripts/check_metrics.py"]
  c23 --> c24
  c25["docs/intent/002"]
  c24 --> c25
  class c6,c12,c16 med
```

### Level 4: Role handoffs

```mermaid
flowchart LR
  classDef high fill:#fde2e1,stroke:#c62828,stroke-width:2px
  classDef med fill:#fff4ce,stroke:#b7791f,stroke-width:2px
  classDef done fill:#e6f4ea,stroke:#2e7d32
  classDef inferred stroke-dasharray:5 5
  r0["AppSec"]
  r1["Engineer"]
  r2["Platform engineer"]
  r3["Product Manager"]
  r4["QA engineer"]
  r5["Reviewer"]
  r6["SRE"]
  r7["TPM"]
  r8["Tech Lead"]
  r0 -- "#7→#9" --> r7
  r1 -- "#14→#17" --> r4
  r1 -. "#8→#25, #12→#28" .-> r6
  r1 -- "#8→#6, #10→#13" --> r8
  r2 -- "#3→#8, #3→#10" --> r1
  r2 -- "#20→#23, #22→#23" --> r5
  r2 -. "#22→#26" .-> r6
  r3 -- "#30→#31 C12" --> r7
  r3 -- "#2→#5" --> r8
  r4 -. "#16→#22" .-> r2
  r6 -- "#29→#30" --> r3
  r6 -- "#26→#27 C11" --> r7
  r7 -. "#9→#10" .-> r1
  r7 -- "#18→#19, #36→#19, #36→#22" --> r2
  r8 -- "#6→#7" --> r0
  r8 -- "#13→#11" --> r1
  r8 -. "#13→#19" .-> r2
  linkStyle 7 stroke:#b7791f,stroke-width:2px
  linkStyle 11 stroke:#b7791f,stroke-width:2px
```

### Level 5: External and non-code

```mermaid
flowchart LR
  classDef high fill:#fde2e1,stroke:#c62828,stroke-width:2px
  classDef med fill:#fff4ce,stroke:#b7791f,stroke-width:2px
  classDef done fill:#e6f4ea,stroke:#2e7d32
  classDef inferred stroke-dasharray:5 5
  i8["#8 HEIC test run (R1)<br/>Tooling<br/>owner simonshenn · need-by 11-04 · committed 11-03"]
  i6["#6 Write design.md: routes, data model,…<br/>11-04→11-04"]
  i8 -- "0 slack" --> i6
  i3["#3 Python 3.12 (D2)<br/>Tooling<br/>owner simonshenn · need-by 11-03 · committed 10-26"]
  i3 -. "Inferred" .-> i8
  i10["#10 App skeleton in plan mode<br/>11-09→11-10"]
  i3 --> i10
  x3["Docker Desktop install (D3, done in #25)<br/>Tooling<br/>owner Simon · need-by 2026-12-14 · committed in #25"]
  i25["#25 Install Docker (RAID D3) and write D…<br/>12-14→12-15"]
  x3 --> i25
  i38["#38 API key and spending limit (D4)<br/>Cost approval · Anthropic Console<br/>owner simonshenn · need-by 12-04 · committed missing<br/>C5"]
  i20["#20 evals.yml and API key secret (RAID D4)<br/>12-04→12-04"]
  i38 --> i20
  i23["#23 Claude PR review, CODEOWNERS, plante…<br/>12-09→12-10"]
  i38 --> i23
  i39["#39 pillow-heif licenses (N1)<br/>Licensing · pillow-heif maintainers<br/>owner missing · need-by 11-16 · committed missing<br/>C1 C6"]
  i12["#12 Upload, storage, and gallery<br/>11-16→11-18"]
  i39 -. "Inferred" .-> i12
  i26["#26 deploy.yml, GHCR, staging and produc…<br/>12-16→12-17"]
  i39 -. "Inferred" .-> i26
  i40["#40 EXIF and GPS metadata (N2)<br/>Privacy · Photo Vault design decision<br/>owner missing · need-by 11-04 · committed missing<br/>C2 C7"]
  i40 -. "Inferred" .-> i6
  i41["#41 read:project token (N3)<br/>Vendor · GitHub<br/>owner missing · need-by 12-07 · committed missing<br/>C3 C8"]
  i22["#22 ci.yml and branch protection with re…<br/>12-07→12-08"]
  i41 -. "Inferred" .-> i22
  i42["#42 Docker Desktop license (N4)<br/>Vendor · Docker Inc.<br/>owner missing · need-by 12-14 · committed missing<br/>C4 C9"]
  i42 -. "Inferred" .-> i25
  class i38,i39,i40,i41,i42 med
  class i39,i40,i41,i42 inferred
```

<!-- END GENERATED -->
