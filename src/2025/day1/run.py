# SPDX-FileCopyrightText: 2025 Yannick Kees
#
# SPDX-License-Identifier: MIT

from math import floor

from src.base_class import riddle

TOTAL_SIZE = 100
START_POINT = 50


class code:
    def __init__(self, instructions: str):
        self.direction = instructions[0]
        self.length = int(instructions[1:])

    def turning(self, pos, turns):
        new_point = pos + self.length if self.direction == "R" else pos - self.length
        turns += abs(floor(pos / TOTAL_SIZE) - floor(new_point / TOTAL_SIZE))
        turns += (new_point % TOTAL_SIZE == 0) and self.direction == "L"
        turns -= pos == 0 and self.direction == "L"
        return new_point % TOTAL_SIZE, turns


class day1(riddle):
    def __init__(self, day, mode):
        super().__init__(day, mode)

    def a(self):
        x = START_POINT
        print(sum(1 for line in self.lines if (x := code(line).turning(x, 0)[0]) == 0))

    def b(self):
        x = START_POINT
        zeros = 0

        for line in self.lines:
            x, zeros = code(line).turning(x, zeros)

        print(zeros)


if __name__ == "__main__":
    x = day1(day=1, mode="full")
    x.a()
    x.b()
