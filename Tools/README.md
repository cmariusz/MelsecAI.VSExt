# Tools

This folder is for your own utility scripts that work with the Melsec GX Works3 Import workspace.

Use it for:

- Automation helpers that call the CLI bridge (`.melsec/cli.json`).
- Scripts that process imported XML files under `MelsecImport/Projects/`.
- Build / validation helpers.
- One-off migration or reporting scripts.

Add a matching `.md` file for every script so other team members (and AI assistants) know what it does and how to run it.

Example scripts:

- `cli_example.py` / `cli_example.md` — shows how to call the Melsec CLI bridge from Python.

> `UserFiles/` (created at workspace root) is the recommended output directory for scripts so generated artifacts are not committed by accident.
