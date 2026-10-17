# CMsoft Import for Melsec — VS Code Extension

[![Version](https://img.shields.io/badge/version-2.1.0-blue)](CHANGELOG.md)
[![VS Code](https://img.shields.io/badge/VS%20Code-%3E%3D1.95.0-blue?logo=visualstudiocode)](https://code.visualstudio.com/)
[![License: Commercial EULA](https://img.shields.io/badge/License-Commercial%20EULA-blue.svg)](LICENSE.md)
[![Platform: Windows](https://img.shields.io/badge/Platform-Windows-0078D6?logo=windows)](https://www.microsoft.com/windows)
[![Author](https://img.shields.io/badge/Author-CMsoft-orange?logo=linkedin)](https://www.linkedin.com/in/mariusz-czyrnek-a33b87a6)

**Bidirectional bridge between VS Code and Mitsubishi GX Works3** — import PLC programs from GX Works3 to local files, edit them with full VS Code + Copilot power, and export changes back. Built on the GX Works3 Open Interface (GXW3OpenIF).

## User Manual

The English user manual ships with the extension and opens inside VS Code, offline: **CMsoft Import for Melsec: Open User Manual**, **CMsoft Import for Melsec: Search the User Manual** (jumps to a chapter or section), the walkthrough *Get Started with CMsoft Import for Melsec*, the links of the empty *Project Structure* view, the **Open Help** button of a failed *Open Project*, and **Manuals** in the shared **CMsoft** status bar item (**Help: CMsoft Manuals…** lists the manuals of all installed CMsoft extensions). It covers installation, setting up the GX Works3 Open Interface, every function with screenshots, a complete worked example with real build errors, the Copilot tools, the CLI bridge, settings, the license and troubleshooting.

## Free and PRO

| Feature                                                              | FREE                           | PRO          |
| -------------------------------------------------------------------- | ------------------------------ | ------------ |
| Open / attach GX Works3 projects, browse the project structure, save | ✅                             | ✅           |
| Import POUs, Global Labels and SDTs from GX Works3 to the workspace  | ✅                             | ✅           |
| Build / Rebuild with build error details                             | ✅                             | ✅           |
| Export from the workspace to GX Works3                               | up to 10 objects per operation | ✅ unlimited |
| Copilot Language Model tools and the `@melsec` chat participant      | ⛔                             | ✅           |
| CLI bridge for scripts and automation                                | ⛔                             | ✅           |
| Prepare Workspace (AI instructions, templates, Tools)                | ⛔                             | ✅           |

- **14-day free trial**, no payment details needed: **CMsoft Import for Melsec: Manage License / Subscription** → *Try for free*.
- Subscription (monthly or yearly, renews automatically) or one-time payment: **CMsoft Import for Melsec: Buy License** — prices on the [pricing page](https://extensions.cmsoft.com.pl/pricing?product=melsec-import). A license covers one Seat (one named user on one activated workstation).
- The license is shown in the shared **CMsoft** status bar item (one item for all installed CMsoft extensions) and in the *Connection* view; both open the license panel. The CMsoft item also lists the user manuals of the installed CMsoft extensions under **Manuals**.

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

### Export to GX Works3 (local files → GX Works3) — FREE up to 10 objects per operation

| Capability                  | Description                                     |
| --------------------------- | ----------------------------------------------- |
| **Export XML File**   | Export a single PLCopen XML file into GX Works3 |
| **Export XML Folder** | Export every XML file in a folder recursively   |

### Build and Diagnostics

| Capability              | Description                                            |
| ----------------------- | ------------------------------------------------------ |
| **Build Project**   | Build the GX Works3 project and report errors/warnings |
| **Rebuild Project** | Rebuild All; a project that was never built gets a new label assignment |

The build messages (POU, message, GX Works3 error code) are read from the GX Works3 **Output** window of the project's own GX Works3 and listed in the Output channel.

### Copilot / AI Agent Integration (PRO)

The extension exposes **Language Model Tools** (prefix `melsec_*`) plus a `@melsec` chat participant:

- **Connection / discovery** — `melsec_connect`, `melsec_disconnect`, `melsec_save_project`, `melsec_refresh`
- **Pull from GX Works3 → workspace** — `melsec_list_objects`, `melsec_import_object`, `melsec_import_project`
- **Push workspace → GX Works3** — `melsec_export_file`
- **Build loop** — `melsec_build`, `melsec_rebuild`

The `@melsec` participant sends your request to the chat model with these tools and runs the tools it calls. Tools that write into GX Works3 (`melsec_export_file`, `melsec_save_project`) ask for confirmation in the chat unless `melsecImport.lmTools.autoConfirmExports` is enabled; the import tools, which overwrite workspace files, always ask.

### External CLI Bridge (PRO)

External scripts can drive the same workflows through a localhost-only JSON bridge. The bridge is opt-in (`melsecImport.cli.enabled`). When enabled, the extension writes `.melsec/cli.json` with host, port and bearer token.

```powershell
# in the workspace folder - PowerShell needs nothing else installed
$s = Get-Content .melsec\cli.json | ConvertFrom-Json
$h = @{ Authorization = "Bearer $($s.token)" }
Invoke-RestMethod -Method Post -Uri "http://$($s.host):$($s.port)/api" -Headers $h -ContentType 'application/json' `
                  -Body '{"command":"list_objects","args":{"category":"sdt"}}'
```

The extension also ships the helper `melsec-cli.js`. It runs on the runtime built into VS Code, so no Node.js is needed; the user manual (section 12.4, **CMsoft Import for Melsec: Open User Manual**) has a ready-made `melsec` PowerShell function for it:

```powershell
melsec current_project --pretty
melsec open_project --projectPath "C:\Projects\MyPlc.gx3" --pretty
melsec import_object --objectName MyBlock --pretty
```

`GET /health` answers without a token. The helper exits with 1 when the bridge reports a failure.

## Requirements

| Requirement         | Version                                              |
| ------------------- | ---------------------------------------------------- |
| **OS**        | Windows 10 / 11                                      |
| **GX Works3** | Installed with GX Works3 Open Interface (GXW3OpenIF) |
| **.NET**      | .NET Framework 4.8 (part of Windows 10 / 11)         |
| **VS Code**   | ≥ 1.95.0                                            |

Nothing else needs to be installed — no Node.js, npm or build tools: the extension comes ready to run, and VS Code provides its runtime.

### GX Works3 Open Interface (GXW3OpenIF)

The extension **requires** the GX Works3 Open Interface (GXW3OpenIF) component from Mitsubishi Electric. Without it the extension cannot communicate with GX Works3.

- Make sure GXW3OpenIF is selected when installing GX Works3. It may be offered as an optional component in the GX Works3 installer.
- The OpenIF DLLs must be present in your GX Works3 installation directory (the default is `C:\Program Files (x86)\MELSOFT\GPPW3`; setting `melsecImport.gxWorks3Path`):
  - `GXW3OpenIF32.dll`, `GXW3OpenIF64.dll` (package *GX Works3 Open I/F*)
- If the DLLs are missing, reinstall GX Works3 and enable the **GX Works3 Open Interface** option.

## Installation

1. Install the extension from the VS Code Marketplace (or `code --install-extension MariuszCzyrnek.melsec-import`), or from the VSIX file you received.
2. Make sure GX Works3 is installed.
3. Open a workspace folder in VS Code.
4. Run **CMsoft Import for Melsec: Prepare Workspace** (PRO) to scaffold `MelsecImport/`, the AI instructions (`.github/instructions/`, sections in `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`) and `.gitignore`.
5. Optionally adjust settings via **File → Preferences → Settings → CMsoft Import for Melsec**.

## Usage

### Preparing the Workspace (PRO)

Before importing for the first time, prepare the workspace so the extension can create the expected folder structure and AI assistant templates:

1. Open VS Code in a workspace folder.
2. Click the **Melsec** icon in the Activity Bar.
3. Click **Prepare Workspace** (folder icon) in the Connection view title bar, or run `CMsoft Import for Melsec: Prepare Workspace`.

The command creates:

```
<Workspace>/
├── .gitignore                        # a section with the Melsec ignores
├── AGENTS.md                         # a section: open agents.md standard instructions
├── CLAUDE.md                         # a section: Claude Code imports the instructions
├── .github/
│   ├── copilot-instructions.md       # a section pointing to the instructions below
│   ├── instructions/
│   │   ├── melsec-import.instructions.md      # AI coding rules for GX Works3 XML files (all files)
│   │   └── melsec-import-cli.instructions.md  # CLI bridge usage for agents/scripts (Tools/)
│   └── ProjectDescription.md         # Living project architecture document (created once)
├── Tools/                            # Your automation scripts (README section, melsec_cli_example.py)
├── UserFiles/                        # Output dir for scripts (git-ignored)
└── MelsecImport/
    ├── .melsec-cache/                # Temporary cache (git-ignored)
    └── Projects/                     # Imported GX Works3 projects
```

The CMsoft add-ons share these files (CMsoft workspace protocol): each keeps its own instructions in files named
after it and **one section** in `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, `.gitignore` and
`Tools/README.md`, between `cmsoft:begin` / `cmsoft:end` markers. Running *Prepare Workspace* again updates this
add-on's section and files only; your own text outside the sections — and a file from which you deleted its
`cmsoft:managed` line — is never touched. Unchanged copies of the templates of earlier versions
(`.github/copilot-instructions.md`, `.github/CLI-instruction.md`, `Tools/cli_example.py`, …) are replaced.

Template files are only created if they do not already exist — existing files are never overwritten.

### Connecting to GX Works3

1. Open VS Code in a workspace folder.
2. Click the **Melsec** icon in the Activity Bar.
3. In the **Connection** view click **Action — Click to connect** (or **Open Project**, the folder icon in the view title bar), or run `CMsoft Import for Melsec: Open Project`.
4. Select a `.gx3` project file.

If GX Works3 is already running with the project open, you can also use **Attach to Open Project** (`CMsoft Import for Melsec: Attach to Open Project`).

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

Without a PRO license one export operation covers up to 10 objects; larger operations ask for a license.

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

- This extension is proprietary commercial software licensed under the [End User License Agreement](LICENSE.md). Versions 1.0.0 and earlier were released under the MIT License and remain MIT-licensed; version 2.0.0 and later are not.
- Redistribution of the extension package by anyone other than the Visual Studio Marketplace and the Open VSX Registry is not permitted.
- Third-party notices for npm/NuGet components are listed in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md); those components keep their own (open-source) licenses.
- For Mitsubishi Electric GX Works3 Open Interface components, use and distribution are subject to Mitsubishi Electric package terms; evaluate those terms for your release scenario.
- Do **not** bundle or redistribute `GXW3OpenIF32.dll`, `GXW3OpenIF64.dll`, or other GX Works3 Open Interface binaries with this extension unless explicitly allowed by Mitsubishi Electric terms.
- End users must provide their own licensed GX Works3 installation and GXW3OpenIF entitlement.

## Disclaimer of Liability

The extension is a development and automation tool, and all imports/exports modify engineering data at your own risk.

To the extent permitted by applicable law, the author is not liable for indirect or consequential damages — production downtime, data loss, project corruption or other consequences — resulting from changes made to GX Works3 projects using this extension, and any other liability is limited. Liability that the law does not allow to exclude (for example for damage caused intentionally, or for death or personal injury) and the statutory rights of consumers are not affected.

**You are responsible for all content the extension moves, converts or generates** — programs, function blocks, functions, global labels, structured data types and PLCopen XML files — regardless of whether you wrote it, the extension generated it, or an AI assistant (GitHub Copilot, `@melsec` chat participant, `melsec_*` language model tools, an agent using the CLI bridge) produced it. **AI-generated code is not reviewed or verified by the author.**

Users are fully responsible for validating, testing, and approving all generated or imported changes before deployment to real machines, production lines, or safety-related systems — and for keeping verified project backups before any export, build or save in GX Works3.

These terms are binding as sections 12 (warranty), 13 (liability) and 14 (your content, generated code and safety-critical use) of the [End User License Agreement](LICENSE.md#14-your-content-generated-code-and-safety-critical-use); where this summary and the agreement differ, the agreement applies.

## Trademarks

This extension is an independent product. It is **not** developed, endorsed, sponsored by or affiliated with Mitsubishi Electric Corporation. *MELSEC* and *GX Works3* are trademarks or registered trademarks of Mitsubishi Electric Corporation, used here solely for identification and interoperability purposes; *for Melsec* in the name *CMsoft Import for Melsec* only states which PLCs and software the extension works with. *Visual Studio Code* is a trademark of Microsoft Corporation.

## License

Proprietary commercial software — see the [End User License Agreement](LICENSE.md).
Copyright © 2026 CMsoft. All rights reserved.

**CMsoft** · [office@cmsoft.com.pl](mailto:office@cmsoft.com.pl) · [shop.cmsoft.com.pl](https://shop.cmsoft.com.pl)

| Document                                        | Purpose                                                    |
| ----------------------------------------------- | ---------------------------------------------------------- |
| [LICENSE.md](LICENSE.md)                         | End User License Agreement (terms of use)                  |
| [TERMS.md](TERMS.md)                             | Terms of sale for paid plans                               |
| [PRIVACY.md](PRIVACY.md)                         | Privacy policy — no telemetry, no project data leaves your machine |
| [SECURITY.md](SECURITY.md)                       | Reporting security vulnerabilities, supported versions     |
| [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) | Third-party components and their licenses                  |

**Versions 1.0.0 and earlier** were published under the MIT License. That grant is irrevocable for those versions and is reproduced in section 20 of [LICENSE.md](LICENSE.md). It does not apply to version 2.0.0 or later.
