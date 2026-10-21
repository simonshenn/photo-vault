# RAID Log: Photo Vault

| ID | Type | Description | Owner | Impact | Mitigation or next step | Date raised | Status |
|---|---|---|---|---|---|---|---|
| D1 | Dependency | GitHub CLI (`gh`) is required for repo, milestone and PR steps. Not installed on the dev machine | Simon | Blocks M0 GitHub tasks | `brew install gh`, then `gh auth login` | 2026-10-21 | Open |
| D2 | Dependency | Python 3.12 is required. Machine has Python 3.9.6 | Simon | Blocks M3 | `brew install python@3.12` | 2026-10-21 | Open |
| D3 | Dependency | Docker is required for the simulated deploy. Not installed | Simon | Blocks M5 | Install Docker Desktop before M5 | 2026-10-21 | Open |
| D4 | Dependency | `ANTHROPIC_API_KEY` repo secret is required for Claude PR review and evals in CI | Simon | Blocks M4 evals and M5 review | Create key with a monthly spending limit, add as repo secret | 2026-10-21 | Open |
| A1 | Assumption | Public repo is acceptable because only code and docs are committed | Simon | Photo exposure if `storage/` is committed | `.gitignore` covers `storage/` and `*.db`. Verify with `git log --stat` at each milestone | 2026-10-21 | Open |
| R1 | Risk | HEIC upload depends on `pillow-heif` support on macOS and in the Docker image | Simon | HEIC uploads fail | Confirm in M2 design. Fall back to JPEG/PNG for v1 if blocked | 2026-10-21 | Open |
