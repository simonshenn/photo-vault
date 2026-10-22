# RAID Log: Photo Vault

| ID | Type | Description | Owner | Impact | Mitigation or next step | Date raised | Status |
|---|---|---|---|---|---|---|---|
| D1 | Dependency | GitHub CLI (`gh`) is required for repo, milestone and PR steps. Not installed on the dev machine | Simon | Blocks M0 GitHub tasks | `brew install gh`, then `gh auth login` | 2026-10-21 | Closed 2026-10-21: installed, logged in as simonshenn |
| D2 | Dependency | Python 3.12 is required. Machine has Python 3.9.6 | Simon | Blocks M3 | `brew install python@3.12` | 2026-10-21 | Open |
| D3 | Dependency | Docker is required for the simulated deploy. Not installed | Simon | Blocks M5 | Install Docker Desktop before M5 | 2026-10-21 | Open |
| D4 | Dependency | `ANTHROPIC_API_KEY` repo secret is required for Claude PR review and evals in CI | Simon | Blocks M4 evals and M5 review | Create key with a monthly spending limit, add as repo secret | 2026-10-21 | Open |
| A1 | Assumption | Public repo is acceptable because only code and docs are committed | Simon | Photo exposure if `storage/` is committed | `.gitignore` covers `storage/` and `*.db`. Verify with `git log --stat` at each milestone | 2026-10-21 | Open |
| R1 | Risk | HEIC upload depends on `pillow-heif` support on macOS and in the Docker image | Simon | HEIC uploads fail | Confirm in M2 design. Fall back to JPEG/PNG for v1 if blocked | 2026-10-21 | Open |
| I1 | Issue | #39 pillow-heif codec licenses (N1) has no owner. Source: dependency check 2026-10-22 C1; DEP-037, DEP-038 | Simon | Blocks #12 (start 2026-11-16) and #26 (start 2026-12-16) | Name an owner for #39. Suggested verifiers: Tech Lead, AppSec | 2026-10-22 | Open |
| I2 | Issue | #40 EXIF and GPS metadata decision (N2) has no owner. Source: C2; DEP-039 | Simon | Blocks #6 design.md (start 2026-11-04) | Name an owner for #40. Suggested verifier: AppSec | 2026-10-22 | Open |
| I3 | Issue | #41 read:project token (N3) has no owner. Source: C3; DEP-040 | Simon | Blocks #22 (start 2026-12-07) | Name an owner for #41. Suggested verifier: Platform engineer | 2026-10-22 | Open |
| I4 | Issue | #42 Docker Desktop license terms (N4) has no owner. Source: C4; DEP-041 | Simon | Blocks #25 (start 2026-12-14) | Name an owner for #42. Suggested verifier: SRE | 2026-10-22 | Open |
| I5 | Issue | #38 API key and spending limit has no Committed date (see D4). Source: C5; DEP-035, DEP-036 | Simon | Need-by 2026-12-04 for #20; also #23 (start 2026-12-09) | Set Committed on #38 on or before 2026-12-04 | 2026-10-22 | Open |
| I6 | Issue | #39 pillow-heif codec licenses has no Committed date. Source: C6; DEP-037, DEP-038 | Simon | Need-by 2026-11-16 for #12 | Set Committed on #39 on or before 2026-11-16. Option: check licenses during #8 (2026-11-03) | 2026-10-22 | Open |
| I7 | Issue | #40 EXIF and GPS metadata decision has no Committed date. Source: C7; DEP-039 | Simon | Need-by 2026-11-04 for #6 | Set Committed on #40 on or before 2026-11-04. Option: decide in #6 or #7 | 2026-10-22 | Open |
| I8 | Issue | #41 read:project token has no Committed date. Source: C8; DEP-040 | Simon | Need-by 2026-12-07 for #22 | Set Committed on #41 on or before 2026-12-07 | 2026-10-22 | Open |
| I9 | Issue | #42 Docker Desktop license has no Committed date. Source: C9; DEP-041 | Simon | Need-by 2026-12-14 for #25 | Set Committed on #42 on or before 2026-12-14 | 2026-10-22 | Open |
| R2 | Risk | Same-day handoff: #12 target 2026-11-18 = #14 start 2026-11-18. Source: C10; DEP-011 | Simon | A #12 slip delays #14 and M3 (due 2026-11-20) | Accept (same role, in order that day), or move #14 start to 2026-11-19 | 2026-10-22 | Open |
| R3 | Risk | Same-day handoff: #26 target 2026-12-17 = #27 start 2026-12-17. Source: C11; DEP-018 | Simon | A #26 slip delays the launch checklist, go/no-go, and M5 (due 2026-12-18) | Accept, or move #27 start to 2026-12-18 (1.25 h fits in one day) | 2026-10-22 | Open |
| R4 | Risk | Same-day handoff: #30 target 2027-01-07 = #31 start 2027-01-07. Source: C12; DEP-021 | Simon | A #30 slip delays the retro and M6 (due 2027-01-08) | Accept (0.5 h decision before the retro), or move #31 start to 2027-01-08 | 2026-10-22 | Open |
| R5 | Risk | Zero slack: #1 target 2026-10-28, #2 start 2026-10-29. Source: C13; DEP-001 | Simon | A #1 slip moves #2 and M1 (due 2026-10-30) | Accept; watch in the 2026-10-30 status | 2026-10-22 | Open |
| R6 | Risk | Zero slack: #5 target 2026-11-03, #6 start 2026-11-04. Source: C14; DEP-003 | Simon | M2 chain: a #5 slip moves #6, #7, #9 and M2 (due 2026-11-06) | Accept; watch M2 in weekly status | 2026-10-22 | Open |
| R7 | Risk | Zero slack: #8 target 2026-11-03, #6 start 2026-11-04. Source: C15; DEP-004 | Simon | M2 chain: an #8 slip moves #6 and M2 | Accept; watch M2 in weekly status | 2026-10-22 | Open |
| R8 | Risk | Zero slack: #6 target 2026-11-04, #7 start 2026-11-05. Source: C16; DEP-005 | Simon | M2 chain: a #6 slip moves #7, #9 and M2 | Accept; watch M2 in weekly status | 2026-10-22 | Open |
| R9 | Risk | Zero slack: #7 target 2026-11-05, #9 start 2026-11-06. Source: C17; DEP-006 | Simon | A #7 slip moves #9 and M2 | Accept; watch M2 in weekly status | 2026-10-22 | Open |
| R10 | Risk | Zero slack: #9 target 2026-11-06, #10 start 2026-11-09 (Inferred link). Source: C18; DEP-024 | Simon | An M2 slip moves the start of M3 | Accept; confirm the Inferred link | 2026-10-22 | Open |
| R11 | Risk | Zero slack: #13 target 2026-11-11, #11 start 2026-11-12. Source: C19; DEP-009 | Simon | M3 chain: a #13 slip moves #11, #12, #14 and M3 (due 2026-11-20) | Accept; watch M3 in weekly status | 2026-10-22 | Open |
| R12 | Risk | Zero slack: #11 target 2026-11-13, #12 start 2026-11-16. Source: C20; DEP-010 | Simon | M3 chain: an #11 slip moves #12, #14 and M3 | Accept; watch M3 in weekly status | 2026-10-22 | Open |
| R13 | Risk | Zero slack: #10 target 2026-11-10, #13 start 2026-11-11. Source: C21; DEP-007 | Simon | M3 chain: a #10 slip moves the whole M3 chain | Accept; watch M3 in weekly status | 2026-10-22 | Open |
| R14 | Risk | Zero slack: #17 target 2026-11-23, #16 start 2026-11-24. Source: C22; DEP-013 | Simon | A #17 slip moves #16 in Thanksgiving week | Accept; watch M4 in weekly status | 2026-10-22 | Open |
| R15 | Risk | Zero slack: #14 target 2026-11-20, #17 start 2026-11-23. Source: C23; DEP-012 | Simon | An M3 slip moves the start of M4 | Accept; watch M3 in weekly status | 2026-10-22 | Open |
| R16 | Risk | Zero slack: #18 target 2026-11-30, #19 start 2026-12-01. Source: C24; DEP-014 | Simon | M4 chain: an #18 slip moves #19, #20 and M4 (due 2026-12-04) | Accept; watch M4 in weekly status | 2026-10-22 | Open |
| R17 | Risk | Zero slack: #19 target 2026-12-03, #20 start 2026-12-04. Source: C25; DEP-015 | Simon | A #19 slip moves #20 and M4 | Accept; watch M4 in weekly status | 2026-10-22 | Open |
| R18 | Risk | Zero slack: #22 target 2026-12-08, #23 start 2026-12-09. Source: C26; DEP-016 | Simon | A #22 slip moves #23 | Accept; watch M5 in weekly status | 2026-10-22 | Open |
| R19 | Risk | Zero slack: #25 target 2026-12-15, #26 start 2026-12-16. Source: C27; DEP-017 | Simon | A #25 slip moves #26, #27 and M5 (due 2026-12-18) | Accept; watch M5 in weekly status | 2026-10-22 | Open |
| R20 | Risk | Zero slack: #28 target 2027-01-04, #29 start 2027-01-05. Source: C28; DEP-019 | Simon | M6 chain: a #28 slip moves #29, #30, #31 and M6 (due 2027-01-08) | Accept; holiday weeks are buffer | 2026-10-22 | Open |
| R21 | Risk | Zero slack: #29 target 2027-01-06, #30 start 2027-01-07. Source: C29; DEP-020 | Simon | A #29 slip moves #30, #31 and M6 | Accept; holiday weeks are buffer | 2026-10-22 | Open |

Entries I1 to I9 and R2 to R21 come from the `scripts/check_deps.py` run on 2026-10-22. Concern IDs (C1 to C29) renumber on each run; the register IDs (DEP-xxx) and issue numbers stay stable.
