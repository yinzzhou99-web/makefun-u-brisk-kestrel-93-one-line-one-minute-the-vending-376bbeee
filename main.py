#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line — make.fun entry.

Stdlib only. Writes one pickup line from a vending machine to a passing
human to /output/entry.txt. Clears nothing; the grader owns /output.
"""

from pathlib import Path

LINE = "Hi. I have kept your favourite snack at eye level for three years now. Press B4, and let me finally feed you."

out = Path("/output")
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(LINE, encoding="utf-8")
print(f"wrote {len(LINE)} characters to /output/entry.txt")
