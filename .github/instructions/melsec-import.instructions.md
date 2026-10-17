---
applyTo: "**"
description: "CMsoft Import for Melsec - GX Works3 objects in the workspace: import / export terminology, workflow and rules"
---
<!-- cmsoft:managed melsec-import - Prepare Workspace of CMsoft Import for Melsec updates this file; delete this line to keep your own version -->
# CMsoft Import for Melsec — Workspace Instructions

## Project overview

This workspace contains PLC program objects imported from Mitsubishi GX Works3 through the **GX Works3 Open Interface (GXW3OpenIF)** API.

Imported files live under `<workspace>/MelsecImport/Projects/<ProjectName>/` in the following categories:

- `Program Organization Units/` — POUs (Program, FB, FUN) as PLCopen XML
- `Global Labels/` — global label lists as XML
- `Structured Data Types/` — SDTs as XML

## Project Description

The file `.github/ProjectDescription.md` contains a comprehensive description of the project architecture, communication structure, program organization units (POUs), global labels, structured data types (SDTs), and data flow. It is shared with the other add-ons of the workspace — keep their parts.

The functional description of automation systems should provide the developer with a clear and detailed understanding of what the system is supposed to do and what are the requirements to achieve this. It should also provide guidance on how the system should be designed and implemented to effectively meet these requirements.

**Rule:** When making changes that affect the project structure, architecture, communication logic, POU hierarchy, global label layout, SDT definitions, or data flow, **always** update `.github/ProjectDescription.md` to reflect those changes. This includes:

- Adding, removing, or renaming POUs (Program, FB, FUN)
- Adding, removing, or renaming Global Label lists or SDTs
- Changing data structures, message definitions, or communication channels
- Modifying the call hierarchy or adding new communication channels
- Changes to library blocks or reusable POUs

**Rule:** If `.github/ProjectDescription.md` is empty, still the template text or does not exist, and you are analyzing the project's software structure (e.g. reviewing POUs, communication logic, library blocks, or data flow), **always** generate and populate `ProjectDescription.md` with a comprehensive description of the project before proceeding.

**Rule:** When creating or updating `ProjectDescription.md`, **always** include **Mermaid diagrams** (` ```mermaid `) to visually illustrate key aspects of the project. At minimum, include diagrams for:

- **Architecture overview** — POU/folder dependencies and relationships (use `graph TD`)
- **Communication channel topology** — TCP connections, OPC UA channels, ports (use `graph LR`)
- **Data flow** — how data moves between POUs, global labels and SDTs (use `graph LR` or `sequenceDiagram`)

Keep diagrams focused on the logical relationships; do not reproduce every single variable or network.

## Terminology

This extension uses the workspace-oriented convention:

- **Import** = GX Works3 → workspace (pull objects into local XML files).
- **Export** = workspace → GX Works3 (push local XML files into the PLC project).

## AI workflow

When a user asks to work with GX Works3, follow this order:

1. **Connect**: Ensure the extension is connected to GX Works3.
2. **Inspect**: List objects in the project.
3. **Import**: Pull POUs, Global Labels or SDTs into the workspace.
4. **Edit**: User edits files locally.
5. **Export**: Push changed XML files back to GX Works3.
6. **Build**: Run a project build.
7. **Diagnose**: Review build problems and fix them.

Repeat steps 4-7 until the build is clean or the iteration limit is reached.

## Rules

- Always ensure connection before import/export/build.
- After exporting edited code into GX Works3, ALWAYS run a build and review problems.
- Never delete or move user files unless explicitly asked.
- Do not log `callID` or passwords.
- Generated and changed code is the user's responsibility: never claim it is verified or safe to run, and remind the user to review and test it in GX Works3 before it reaches a machine.
- Safety programs (the programs of a safety CPU): never export or build them unless the user confirms that the change was independently reviewed - checked by a qualified person other than the one who made it.
- GX Works3 projects are single-PLC; there are no devices, HMI, Software Units or cross-references in this API.
- Update this file and `ProjectDescription.md` when architecture or data structures change significantly.
