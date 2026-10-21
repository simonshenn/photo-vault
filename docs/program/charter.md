# Program Charter: Photo Vault

| Field | Value |
|---|---|
| Owner | Simon |
| Date raised | 2026-10-21 |
| Status | Draft |
| Target completion | Owner to set |

## Goal

Build a private photo website for one user and run it through every phase of
the AI-native SDLC, so each phase produces a working result and a learning-log
entry.

## Scope

In scope for v1: single-user login, photo upload (JPEG, PNG, HEIC), thumbnail
gallery, view and delete a photo, local run, simulated deploy.

Out of scope for v1: multiple users, sharing links, cloud hosting, albums.

## Milestones

Target dates are owner to set. Each milestone maps to a GitHub Milestone.

| ID | Phase | Exit criteria | Target date |
|---|---|---|---|
| M0 | Setup | Repo on GitHub, charter and learning log committed | Owner to set |
| M1 | Plan | `docs/intent/001-photo-vault.md` merged | Owner to set |
| M2 | Design | `docs/requirements.md` and `docs/design.md` merged through a PR | Owner to set |
| M3 | Build | Login, upload, gallery, delete work locally. CLAUDE.md and skills committed | Owner to set |
| M4 | Test | Tests and hooks run on every edit. Evals run in CI | Owner to set |
| M5 | Deploy | Claude PR review, approval hook, and deploy workflow with approval gate | Owner to set |
| M6 | Maintain | Metrics check drafts a new intent file. Retro written | Owner to set |

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
| Status report | Weekly (owner to confirm day) | `docs/program/status/YYYY-MM-DD.md` |
| RAID review | Weekly, with status | `docs/program/raid.md` |
| Retro | End of each cycle (after M6) | `docs/program/retro-NNN.md` |
