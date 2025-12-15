# SPDX-FileCopyrightText: 2025 Yannick Kees
#
# SPDX-License-Identifier: MIT

import functools

from src.base_class import riddle


class day(riddle):
    def __init__(self, day, mode):
        super().__init__(day, mode)
        self.children = {"out": []}

        for line in self.lines:
            curr, child = line.split(":")
            self.children[curr] = child[1:].split(" ")

    @functools.cache
    def ways_to_get_to_out(self, n: str, dac=False, fft=False) -> int:
        if n == "out":
            return 1 if dac and fft else 0

        return sum(
            self.ways_to_get_to_out(c, dac or n == "dac", fft or n == "fft")
            for c in self.children[n]
        )

    def a(self):
        print(self.ways_to_get_to_out("you", True, True))

    def b(self):
        print(self.ways_to_get_to_out("svr", False, False))


if __name__ == "__main__":
    x = day(day=11, mode="full")
    x.a()
    x.b()
