#!/usr/bin/env python3
# cmsoft:managed melsec-import - Prepare Workspace of CMsoft Import for Melsec updates this file; delete this line to keep your own version
"""Minimal example client for the CMsoft Import for Melsec CLI bridge."""

import json
import pathlib
import urllib.request


def read_state(workspace: pathlib.Path) -> dict:
    state_path = workspace / ".melsec" / "cli.json"
    with state_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def api_call(state: dict, command: str, args: dict | None = None) -> dict:
    url = f"http://{state['host']}:{state['port']}/api"
    payload = json.dumps({"command": command, "args": args or {}}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {state['token']}",
        },
        method="POST",
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main() -> None:
    # Adjust if your workspace is elsewhere.
    workspace = pathlib.Path(__file__).resolve().parent.parent
    state = read_state(workspace)

    print("Current project:")
    print(json.dumps(api_call(state, "current_project"), indent=2))

    print("\nObjects:")
    print(json.dumps(api_call(state, "list_objects", {"category": "all"}), indent=2))


if __name__ == "__main__":
    main()
