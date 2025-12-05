# SPDX-FileCopyrightText: 2025 Yannick Kees
#
# SPDX-License-Identifier: MIT


from pathlib import Path

from src.base_class import riddle


class my_range:
    def __init__(self, code):
        self.a, self.b = map(int, code.split("-"))

    def val(self, x):
        return self.a <= x <= self.b

    def size(self):
        return abs(self.b - self.a) + 1


class day(riddle):
    def __init__(self, day, mode):
        super().__init__(day, mode)

        with Path.open(self.filename, encoding="utf-8") as f:
            parts = f.read().strip().split("\n\n")  # split at blank line

        self.ranges = [my_range(x) for x in parts[0].splitlines()]
        self.numbers = parts[1].splitlines()

    def checking(self, x, ranges):
        return int(any(single_range.val(x) for single_range in ranges))

    def a(self):
        print(sum([self.checking(int(x), self.ranges) for x in self.numbers]))

    def b(self):
        final_ranges = []

        for x in sorted(self.ranges, key=lambda x: x.a):

            if self.checking(x.a, final_ranges):
                final_ranges[-1].b = max(final_ranges[-1].b, x.b)
            else:
                final_ranges.append(x)

        print(sum([x.size() for x in final_ranges]))


if __name__ == "__main__":
    x = day(day=5, mode="full")
    x.a()  # 701
    x.b()  # 352340558684863
