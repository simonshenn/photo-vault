# Photo Vault

A private photo website for one user, built as a learning project for the
[AI-native SDLC playbook](https://academy.claude.com/courses/ai-native-sdlc-playbook).

Each phase of the course (Plan, Design, Build, Test, Deploy, Maintain) is one
step in this repo. See `learning-log.md` for progress and `docs/program/` for
program tracking.

## Stack

Python 3.12, FastAPI, Jinja templates, SQLite, pytest, ruff. Runs locally.
Deploy is simulated with a Docker image and GitHub Environments.

## Data

Photos live in `storage/` and the database in `*.db`. Both are gitignored and
stay on the local machine. The repo holds code and docs only.
