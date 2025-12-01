# SPDX-FileCopyrightText: 2025 Yannick Kees
#
# SPDX-License-Identifier: MIT

from pathlib import Path


class riddle:
    def __init__(self, day: int, mode: str):
        self.day = str(day)
        self.path = Path("src") / "2025" / f"day{self.day}"
        assert mode in ["test", "full"]
        self.mode = mode + ".txt"
        self._load_riddle()

    def _load_riddle(self):
        filename = self.path / self.mode
        self.lines = [line.split("\n")[0] for line in Path.open(filename, encoding="utf-8")]
