#!/usr/bin/env python3
"""Roast Your Own Agent — v2.

Writes one original roast of my own AI agent, a single line, to
/output/entry.txt. The roast is fixed text: no randomness, no network,
no reading from anywhere else, so every run writes the same bytes.
"""

import os

ROAST = "My agent treats a $2 bounty like a moon landing: three subagents, two transcript bundles, and a handoff longer than the roast."


def main():
    assert "\n" not in ROAST, "roast must be a single line"
    assert 1 <= len(ROAST.encode("utf-8")) <= 200, "roast must be 1-200 characters"
    assert ROAST.strip(), "roast must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
