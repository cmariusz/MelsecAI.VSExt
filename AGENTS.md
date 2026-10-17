## CMsoft Import for Melsec

GX Works3 projects are imported into `MelsecImport/Projects/` and exported back with the **CMsoft Import for
Melsec** VS Code extension. Read before working with GX Works3 files:

- [.github/instructions/melsec-import.instructions.md](.github/instructions/melsec-import.instructions.md) —
  the AI workflow (connect → inspect → import → edit → export → build) and the rules;
- [.github/instructions/melsec-import-cli.instructions.md](.github/instructions/melsec-import-cli.instructions.md) —
  the CLI bridge for scripts and agents (`.melsec/cli.json`).

Conventions:

- **Import** = GX Works3 → workspace (pull objects into local XML files).
- **Export** = workspace → GX Works3 (push local XML files into the PLC project).
- Keep changes minimal and follow the existing code style.
- Do not add HMI, Software Unit or full HW config features — GXW3OpenIF does not support them.
