# Program Charter: Photo Vault

| Field | Value |
|---|---|
| Owner | Simon |
| Date raised | 2026-10-21 |
| Status | Draft |
| Target completion | 2027-01-08 (approved 2026-10-21; basis: M6 roll-up below) |

## Goal

Build a private photo website for one user and run it through every phase of
the AI-native SDLC, so each phase produces a working result and a learning-log
entry.

## Scope

In scope for v1: single-user login, photo upload (JPEG, PNG, HEIC), thumbnail
gallery, view and delete a photo, local run, simulated deploy.

Out of scope for v1: multiple users, sharing links, cloud hosting, albums.

## Milestones

Each milestone maps to a GitHub Milestone. Dates approved 2026-10-21. Basis:
issue estimates rolled up at 5 h per week (range 4 to 6), start 2026-10-26.
Issue breakdown and estimates live on the
[Project board](https://github.com/users/simonshenn/projects/1).

| ID | Phase | Exit criteria | Estimate | Target date | Notes |
|---|---|---|---|---|---|
| M0 | Setup | Repo on GitHub, charter and learning log committed | | 2026-10-21 | Done |
| M1 | Plan | `docs/intent/001-photo-vault.md` merged | 3.5 h | 2026-10-30 | 1 week |
| M2 | Design | `docs/requirements.md` and `docs/design.md` merged through a PR | 6.0 h | 2026-11-06 | 1 week, top of range |
| M3 | Build | Login, upload, gallery, delete work locally. CLAUDE.md and add-route skill committed | 11.5 h | 2026-11-20 | 2 weeks, about 5.75 h per week |
| M4 | Test | Tests and hooks run on every edit. Weekly-status skill and evals run in CI | 10.0 h | 2026-12-04 | 2 weeks. Includes Thanksgiving week |
| M5 | Deploy | Claude PR review, approval hook, and deploy workflow with approval gate | 9.5 h | 2026-12-18 | 2 weeks |
| M6 | Maintain | Metrics check drafts a new intent file. Retro written | 5.0 h | 2027-01-08 | 3 weeks, Dec 21 to Jan 1 assumed light |

Slip rule: if M2 or M3 slips one week, M4 and M5 move one week each. M5 then
lands 2026-12-25 and M6 holds at 2027-01-08 by using one holiday week.

## RACI

Simon fills every role in this project. The second column shows who owns the
work at a large SaaS company.

| Activity | This project | Large SaaS company |
|---|---|---|
| Intent and success measures | Simon (R/A) | PM (R/A), Tech Lead (C), TPM (C) |
| Requirements and design | Simon (R/A) | Tech Lead (R), Architect or EM (A), AppSec and SRE (C) |
| Build | Simon with Claude (R), Simon (A) | Engineers (R), Tech Lead (A) |
| Tests and evals | Simon with Claude (R), Simon (A) | SDET/QA and Platform (R), QA Lead or EM (A) |
| PR review | Claude (R), Simon (A) | Peer engineers (R), AppSec (C) |
| Release approval | Simon (R/A) | Release Manager or SRE (R), EM or CAB (A) |
| Metrics review | Simon (R/A) | SRE (R), PM (A), TPM (runs cadence) |
| Program tracking and status | Simon (R/A), Claude drafts | TPM (R/A), stakeholders (I) |

## Cadence

| Activity | Frequency | Output |
|---|---|---|
| Status report | Weekly, Fridays | `docs/program/status/YYYY-MM-DD.md` |
| RAID review | Weekly, with status | `docs/program/raid.md` |
| Retro | End of each cycle (after M6) | `docs/program/retro-NNN.md` |
