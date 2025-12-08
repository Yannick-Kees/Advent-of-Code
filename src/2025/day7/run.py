# SPDX-FileCopyrightText: 2025 Yannick Kees
#
# SPDX-License-Identifier: MIT

import numpy as np

from src.base_class import riddle


class day(riddle):
    def __init__(self, day, mode):
        super().__init__(day, mode)
        my_dict = {"^": -1, "S": 1, ".": 0}
        self.input_lines = np.array(
            [[my_dict[y] for y in list(x.replace("\n", ""))] for x in self.lines],
        )

        self.splits = 0
        for i, line in enumerate(self.input_lines[1:]):
            for j, _ in enumerate(line):
                if self.input_lines[i, j] >= 1:
                    if self.input_lines[i + 1, j] == -1:
                        self.splits += 1
                        self.input_lines[i + 1, j + 1] += self.input_lines[i, j]
                        self.input_lines[i + 1, j - 1] += self.input_lines[i, j]
                    else:
                        self.input_lines[i + 1, j] += self.input_lines[i, j]

    def a(self):
        print(self.splits)

    def b(self):
        print(sum([int(x) for x in self.input_lines[-1]]))


if __name__ == "__main__":
    x = day(day=7, mode="full")
    x.a()
    x.b()
