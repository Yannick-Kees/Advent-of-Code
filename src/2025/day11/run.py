# SPDX-FileCopyrightText: 2025 Yannick Kees
#
# SPDX-License-Identifier: MIT

from src.base_class import riddle

import functools

@functools.cache
def ways_to_get_to_out(n: str, dac = False, fft = False) -> int:
    if n == "out":
        return 1 if dac and fft else 0

    if n == "dac":
        dac = True
    if n == "fft":
        fft = True

    return sum(ways_to_get_to_out(c, dac, fft) for c in children[n])


class day(riddle):
    def __init__(self, day, mode):
        super().__init__(day, mode)
        children = {"out": []}

        for line in self.lines:
            curr, child = line.split(":")
            children[curr] = child[1:].split(" ")

    def a(self):
        print(ways_to_get_to_out("you", True, True))

    def b(self):
        print(ways_to_get_to_out("svr", False, False))


if __name__ == "__main__":
    x = day(day=11, mode="full")
    x.a()
    x.b()
