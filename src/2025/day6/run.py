# SPDX-FileCopyrightText: 2025 Yannick Kees
#
# SPDX-License-Identifier: MIT

from math import prod
from pathlib import Path

import numpy as np

from src.base_class import riddle


class math_code:
    def __init__(self, line):
        self.add = line[-1] == "+"
        self.values = map(int, (line[:-1]))

    def compute(self):
        return sum(self.values) if self.add else prod(self.values)


class new_code(math_code):
    def __init__(self, line):
        self.add = line[0][-1] == "+"
        self.values = list(
            map(
                int,
                [
                    "".join(character[:-1])
                    for character in line
                    if "".join(character[:-1]).replace(" ", "") != ""
                ],
            ),
        )


class day(riddle):
    def __init__(self, day, mode):
        super().__init__(day, mode)

    def a(self):
        print(open("src/2025/day6/test.txt"))
        print(self.lines)
        matrix = np.array(
            [list(filter(None, (x.replace("  ", " ").split(" ")))) for x in self.lines],
        ).T
        print(sum([math_code(x).compute() for x in matrix]))

    def b(self):
        matrix = np.array([list(x) for x in Path.open("src/2025/day6/full.txt").readlines()]).T
        blank_rows = np.where(np.all(matrix == " ", axis=1))[0]
        splits = np.split(matrix, blank_rows + 1)
        print(sum([new_code(s).compute() for s in splits]))


if __name__ == "__main__":
    x = day(day=6, mode="full")
    x.a()
    # x.b()
