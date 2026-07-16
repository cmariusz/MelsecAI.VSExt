# CLI Example — Melsec GX Works3 Import

`cli_example.py` is a minimal Python client for the Melsec CLI bridge.

## Requirements

- Python 3.8+
- The Melsec CLI bridge must be enabled in VS Code (`melsecImport.cli.enabled` or click **CLI Bridge** in the Connection view).

## What it does

1. Reads the connection token from `.melsec/cli.json` in the workspace.
2. Calls the `current_project` command to verify the connection.
3. Calls `list_objects` to show available POUs, Global Labels and SDTs.

## Usage

```powershell
python Tools/cli_example.py
```

## Safety

- The bridge binds only to `127.0.0.1`.
- Read `.melsec/cli.json` at runtime — do not hard-code the token.
- Do not commit `.melsec/cli.json`.
