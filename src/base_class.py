# SPDX-FileCopyrightText: 2025 Yannick Kees
#
# SPDX-License-Identifier: MIT

from pathlib import Path


class riddle:
    def __init__(self, day: int, mode: str) -> None:
        self.day = str(day)
        self.path = Path("src") / "2025" / f"day{self.day}"
        self.mode = mode + ".txt"
        self._load_riddle()

    def _load_riddle(self) -> None:
        self.filename = self.path / self.mode
        self.lines = [line.split("\n")[0] for line in Path.open(self.filename, encoding="utf-8")]
