# Melsec GX Import — VS Code Extension

[![Version](https://img.shields.io/badge/version-0.1.143-blue)](package.json)
[![VS Code](<https://img.shields.io/badge/VS%20Code-%3E%3D1.95.0-blue?logo=visualstudiocode>)](https://code.visualstudio.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform: Windows](https://img.shields.io/badge/Platform-Windows-0078D6?logo=windows)](https://www.microsoft.com/windows)
[![Author](https://img.shields.io/badge/Author-Mariusz%20Czyrnek-orange?logo=linkedin)](https://www.linkedin.com/in/mariusz-czyrnek-a33b87a6)
[![Donate with PayPal](https://img.shields.io/badge/Donate-PayPal-00457C?logo=paypal&logoColor=white)](https://www.paypal.com/donate/?hosted_button_id=68KF5N2K5QQVY)

**Bidirectional bridge between VS Code and Mitsubishi GX Works3** — import PLC programs from GX Works3 to local files, edit them with full VS Code + Copilot power, and export changes back. Built on the GX Works3 Open Interface (GXW3OpenIF).

If this extension helps your Melsec GX Works3 workflow, you can support ongoing development with a voluntary [PayPal donation](https://www.paypal.com/donate/?hosted_button_id=68KF5N2K5QQVY).

## Key Features

### Import from GX Works3 (GX Works3 → local files)

| Capability                      | Description                                                      |
| ------------------------------- | ---------------------------------------------------------------- |
| **Connect to GX Works3**  | Open a project file (`.gx3`) directly or through a file dialog |
| **Import Entire Project** | Import POUs, Global Labels and SDTs from the current project     |
| **Import POUs**           | Import Program, FB and FUN blocks as PLCopen XML                 |
| **Import Global Labels**  | Import global label lists as XML                                 |
| **Import SDTs**           | Import structured data types as XML                              |
| **Project Explorer**      | Browse the GX Works3 project hierarchy in the VS Code sidebar    |

### Export to GX Works3 (local files → GX Works3)

| Capability                  | Description                                     |
| --------------------------- | ----------------------------------------------- |
| **Export XML File**   | Export a single PLCopen XML file into GX Works3 |
| **Export XML Folder** | Export every XML file in a folder recursively   |

### Build and Diagnostics

| Capability              | Description                                            |
| ----------------------- | ------------------------------------------------------ |
| **Build Project** | Build the GX Works3 project and report errors/warnings |
| **Get Problems**  | Show build diagnostics for the model to fix            |

### Copilot / AI Agent Integration

The extension exposes **Language Model Tools** (prefix `melsec_*`) plus a `@melsec` chat participant:

- **Connection / discovery** — `melsec_connect`, `melsec_disconnect`, `melsec_save_project`, `melsec_refresh`
- **Pull from GX Works3 → workspace** — `melsec_list_objects`, `melsec_import_object`, `melsec_import_project`
- **Push workspace → GX Works3** — `melsec_export_file`
- **Build loop** — `melsec_build`, `melsec_rebuild`

Exports that overwrite existing GX Works3 objects show a confirmation dialog unless `melsecImport.lmTools.autoConfirmExports` is enabled.

### External CLI Bridge

External scripts can drive the same workflows through a localhost-only JSON bridge. The bridge is opt-in (`melsecImport.cli.enabled`). When enabled, the extension writes `.melsec/cli.json` with host, port and bearer token.

```powershell
npm run melsec:cli -- current_project --pretty
npm run melsec:cli -- open_project --filePath "C:\Projects\MyPlc.gx3" --pretty
npm run melsec:cli -- import_object --objectName MyBlock --objectType pou --pretty
```

## Requirements

| Requirement         | Version                                              |
| ------------------- | ---------------------------------------------------- |
| **OS**        | Windows 10 / 11                                      |
| **GX Works3** | Installed with GX Works3 Open Interface (GXW3OpenIF) |
| **.NET**      | .NET Framework 4.8 (runtime), .NET 8 SDK (build)     |
| **VS Code**   | ≥ 1.95.0                                            |
| **Node.js**   | 20+ (for building / packaging only)                  |

### GX Works3 Open Interface (GXW3OpenIF)

The extension **requires** the GX Works3 Open Interface (GXW3OpenIF) component from Mitsubishi Electric. Without it the extension cannot communicate with GX Works3.

- Make sure GXW3OpenIF is selected when installing GX Works3. It may be offered as an optional component in the GX Works3 installer.
- The OpenIF DLLs must be present in your GX Works3 installation directory, e.g.:
  - `C:\Program Files\MELSOFT\GX Works3\GXW3OpenIF32.dll`
  - `C:\Program Files\MELSOFT\GX Works3\GXW3OpenIF64.dll`
- If the DLLs are missing, reinstall GX Works3 and enable the **GX Works3 Open Interface** option.

## Installation

1. Install the extension from the VSIX or build from source.
2. Make sure GX Works3 is installed.
3. Open a workspace folder in VS Code.
4. Run **Melsec Import: Prepare Workspace** to scaffold `MelsecImport/`, `.github/`, `AGENTS.md`, `CLAUDE.md` and `.gitignore`.
5. Optionally adjust settings via **File → Preferences → Settings → Melsec GX Works3 Import**.

## Usage

### Preparing the Workspace

Before importing for the first time, prepare the workspace so the extension can create the expected folder structure and AI assistant templates:

1. Open VS Code in a workspace folder.
2. Click the **Melsec** icon in the Activity Bar.
3. Click **Prepare Workspace** (folder icon) in the Connection view title bar, or run `Melsec Import: Prepare Workspace`.

The command creates:

```
<Workspace>/
├── .gitignore                        # Melsec-specific ignores
├── AGENTS.md                         # Open agents.md standard instructions
├── CLAUDE.md                         # Claude Code instructions
├── .github/
│   ├── copilot-instructions.md       # AI coding rules for GX Works3 XML files
│   ├── CLI-instruction.md            # CLI bridge usage for agents/scripts
│   └── ProjectDescription.md         # Living project architecture document
├── Tools/                            # Your automation scripts (with examples)
├── UserFiles/                        # Output dir for scripts (git-ignored)
└── MelsecImport/
    ├── .melsec-cache/                # Temporary cache (git-ignored)
    └── Projects/                     # Imported GX Works3 projects
```

Template files are only created if they do not already exist — existing files are never overwritten.

### Connecting to GX Works3

1. Open VS Code in a workspace folder.
2. Click the **Melsec** icon in the Activity Bar.
3. Click **Open Project** or run `Melsec Import: Open Project`.
4. Select a `.gx3` project file.

If GX Works3 is already running with the project open, you can also use **Attach to Open Project** (`Melsec Import: Attach to Open Project`).

### Importing from GX Works3

1. Connect to GX Works3.
2. Browse the project structure in the **Melsec Project Explorer** sidebar.
3. Right-click on any node to import POUs, Global Labels or SDTs.
4. Files are saved under `MelsecImport/Projects/<ProjectName>/` in your workspace.

### Exporting to GX Works3

1. Connect to GX Works3.
2. In the VS Code Explorer, right-click an XML file or folder.
3. Choose **Export to GX Works** or **Export All Objects to GX Works**.
4. Objects are exported into the open project.

## Architecture

```
VS Code Extension (TypeScript)
    ↓ electron-edge-js / edge-js
MelsecOpenIFBridge (.NET Framework 4.8)
    ↓ GXW3OpenIF32/64.dll
GX Works3 Open Interface
    ↓ GX Works3 IDE / PLC
```

## Third-Party Licensing & Redistribution

- This extension code is released under [MIT](LICENSE).
- Third-party notices for npm/NuGet components are listed in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
- For Mitsubishi Electric GX Works3 Open Interface components, use and distribution are subject to Mitsubishi Electric package terms; evaluate those terms for your release scenario.
- Do **not** bundle or redistribute `GXW3OpenIF32.dll`, `GXW3OpenIF64.dll`, or other GX Works3 Open Interface binaries with this extension unless explicitly allowed by Mitsubishi Electric terms.
- End users must provide their own licensed GX Works3 installation and GXW3OpenIF entitlement.

## Disclaimer of Liability

The extension is a development and automation tool, and all imports/exports modify engineering data at your own risk.

The author is not liable for any direct or indirect damages, production downtime, data loss, project corruption, safety incidents, or other consequences resulting from changes made to GX Works3 projects using this extension.

Users are fully responsible for validating, testing, and approving all generated or imported changes before deployment to real machines, production lines, or safety-related systems.

## License

[MIT](LICENSE) — Copyright (c) 2026 Mariusz Czyrnek
