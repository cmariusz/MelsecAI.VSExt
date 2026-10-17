# Third-Party Notices

This project includes third-party components. Redistribution of this extension should preserve the applicable third-party license notices and terms.

> Informational notice: this file is a practical compliance aid and not legal advice.

## Project License

- This extension is proprietary commercial software licensed under the End User License Agreement (see `LICENSE.md`). Versions 1.0.0 and earlier were released under the MIT License and remain MIT-licensed; version 2.0.0 and later are not.
- The third-party components below keep their own licenses.

## Runtime dependencies (Node.js)

- `edge-js` (^25.0.1) — Apache-2.0
- `electron-edge-js` (>=8.2.2) — MIT
- `xml2js` (^0.6.2) — MIT
- Transitive:
  - `@agracio/edge-cs` — MIT
  - `edge-cs` — Apache
  - `nan` — MIT
  - `sax` — BlueOak-1.0.0
  - `xmlbuilder` — MIT

## .NET wrapper dependencies (NuGet)

- `Newtonsoft.Json` (13.0.3) — MIT
- `Microsoft.CSharp` (4.7.0) — MIT
- `System.Windows.Forms` — Microsoft .NET library license terms (part of Windows/.NET Framework)

## Mitsubishi Electric GX Works3 Open Interface (critical)

- `GXW3OpenIF32.dll` — provided by the GX Works3 installation
- `GXW3OpenIF64.dll` — provided by the GX Works3 installation
- Related Mitsubishi Electric libraries referenced from the GX Works3 installation directory

These libraries are provided by Mitsubishi Electric and are subject to the GX Works3 end-user license agreement and/or applicable Mitsubishi Electric software terms.

### Distribution policy for this extension

1. Do **not** redistribute `GXW3OpenIF32.dll`, `GXW3OpenIF64.dll`, or other GX Works3 Open Interface binaries as part of this extension package unless Mitsubishi Electric terms explicitly allow it for your exact scenario.
2. Require end users to have their own valid GX Works3 installation and GXW3OpenIF entitlement.
3. Keep Mitsubishi Electric package notices and terms available to recipients.
4. Verify export-control and regional restrictions where applicable.

## Recommended compliance checklist

- Keep this `THIRD_PARTY_NOTICES.md` file in source and packaged artifacts.
- Preserve the project `LICENSE` file.
- Do not remove third-party copyright/license notices from redistributed artifacts.
- Re-run dependency license checks before each release (`npm` and `dotnet`) because dependency graphs can change.

## Audit basis (current snapshot)

- Node dependencies from `package.json` and installed `node_modules` metadata.
- .NET dependencies from `dotnet/MelsecOpenIFBridge/MelsecOpenIFBridge.csproj`, `dotnet/MelsecOutputScraper/MelsecOutputScraper.csproj`, and `dotnet list package --include-transitive`.
- Public NuGet package pages for license details where exposed.
