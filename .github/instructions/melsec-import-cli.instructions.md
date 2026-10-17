---
applyTo: "Tools/**"
description: "CMsoft Import for Melsec - the CLI bridge for scripts and agents"
---
<!-- cmsoft:managed melsec-import - Prepare Workspace of CMsoft Import for Melsec updates this file; delete this line to keep your own version -->
# Melsec CLI Bridge Instructions

The CMsoft Import for Melsec extension exposes a localhost-only JSON bridge for external scripts and agents.

## State File

The CLI bridge is **opt-in and disabled by default**. Until it is enabled, no listener runs and no `.melsec/` folder is created.

Enable it in any of these ways:

- Click the **CLI Bridge** row in the *Melsec Connection* view (toggles between `Off` / `On`).
- Click the **terminal** icon (*CMsoft Import for Melsec: Start CLI Bridge*) in the *Melsec Connection* view title bar and confirm the prompt.
- Run **CMsoft Import for Melsec: Toggle CLI Bridge** from the Command Palette.
- Set `melsecImport.cli.enabled` to `true` in VS Code Settings.

Once enabled, the extension writes:

```json
{
  "version": 1,
  "host": "127.0.0.1",
  "port": 58469,
  "token": "..."
}
```

Default location: `.melsec/cli.json` in the workspace.

Rules:

- Read `.melsec/cli.json` at runtime before every automation session.
- Do not hard-code the port or token.
- Do not commit `.melsec/cli.json`.
- Re-read the state file after VS Code reloads or after the bridge is re-enabled.
- If the file is missing, the bridge is disabled — enable `melsecImport.cli.enabled` and retry.

## Request Shape

Send authenticated requests to `POST /api`:

```json
{
  "command": "list_objects",
  "args": {}
}
```

Use `Authorization: Bearer <token>` from `.melsec/cli.json`.

`GET /health` returns `{"success": true, "status": "ok", "commands": [...]}` and does not require a token.

The parameters go in `args` (the bridge also accepts `params`).

## Helper

Nothing has to be installed to call the bridge - PowerShell is enough:

```powershell
$s = Get-Content .melsec\cli.json | ConvertFrom-Json
$h = @{ Authorization = "Bearer $($s.token)" }
Invoke-RestMethod -Method Post -Uri "http://$($s.host):$($s.port)/api" -Headers $h -ContentType 'application/json' `
                  -Body '{"command":"list_objects","args":{"category":"pou"}}'
```

`Tools/melsec_cli_example.py` is a complete Python client of the same protocol (standard library only).

The extension also ships a small helper, `scripts\melsec-cli.js` in its installation folder
(`%USERPROFILE%\.vscode\extensions\mariuszczyrnek.melsec-import-<version>\`). It runs on the runtime built into VS Code, so no
Node.js is needed: section 12.4 of the user manual (**CMsoft Import for Melsec: Open User Manual**) defines a `melsec`
PowerShell function for it. Use `melsec` only when that function exists in the user's PowerShell; otherwise call the bridge as above.
Run it in the workspace folder (it reads `.melsec/cli.json` there, or pass `--workspace <folder>`); parameters are `key=value` or `--key value`:

```powershell
melsec current_project --pretty
melsec get_logs --limit 100 --pretty
melsec list_objects --category pou --pretty
melsec open_project --projectPath "C:\Projects\Demo.gx3" --pretty
```

The helper exits with 0 when the bridge answered with success and with 1 otherwise.

## Commands

Command names mirror the Language Model tools:

| Command | Purpose |
| --- | --- |
| `open_project` | Open a GX Works3 project by `projectPath` (`filePath` is accepted too) without showing a project picker. |
| `disconnect` | Disconnect from GX Works3; the project stays open in GX Works3. |
| `close_project` | Save and close the project in GX Works3, then disconnect. |
| `save_project` | Save the currently open GX Works3 project. |
| `current_project` | Return connection and active project metadata. |
| `list_objects` | List POUs, Global Labels and SDTs in the current project. |
| `import_object` | Pull a single object from GX Works3 to the workspace (`objectName`; `objectType` optional). |
| `import_project` | Pull every object from the current project; `data.removed` lists the files of objects no longer in GX Works3 that went to the recycle bin. |
| `export_file` | Push a single PLCopen XML file into GX Works3. |
| `build` | Build the current project. |
| `rebuild` | Rebuild the current project. |
| `refresh` | Re-read the project structure and refresh the tree; returns the number of objects. |
| `get_logs` | Return recent extension log entries. |

## Recommended Agent Workflow

1. Call `current_project`.
2. If not connected, call `open_project` with the `.gx3` file path.
3. Call `refresh` and `list_objects` before choosing object names.
4. Prefer narrow import scopes; use `import_object` for single objects and `import_project` for full projects.
5. After every export, call `build` and inspect `get_logs` / build results.
6. Use `get_logs` when GX Works3 or the wrapper reports ambiguous failures.

## Safety

- The bridge binds only to `127.0.0.1`.
- Every `POST /api` request requires the per-session token.
- Write operations modify the active GX Works3 project; keep scopes explicit.
- Validate imported/exported PLC changes in GX Works3 before downloading to hardware.
