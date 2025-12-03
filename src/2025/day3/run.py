# SPDX-FileCopyrightText: 2025 Yannick Kees
#
# SPDX-License-Identifier: MIT


from src.base_class import riddle

def find_largest_joltage_recursive(sequence, k=12):
    if k == 0:
        return ""

    largest_digit = max(sequence[: len(sequence) - k + 1])
    best_index = sequence.index(largest_digit)

    remaining = find_largest_joltage_recursive(sequence[best_index + 1 :], k - 1)

    return largest_digit + remaining


class day(riddle):
    def __init__(self, day, mode):
        super().__init__(day, mode)

    def a(self, k=2):
        print(sum([int(find_largest_joltage_recursive(line, k=k)) for line in self.lines]))

    def b(self):
        self.a(k=12)


if __name__ == "__main__":
    x = day(day=3, mode="full")
    x.a()
    x.b()