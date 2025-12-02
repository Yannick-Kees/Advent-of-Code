# SPDX-FileCopyrightText: 2025 Yannick Kees
#
# SPDX-License-Identifier: MIT


from src.base_class import riddle


class code:
    def __init__(self, section):
        self.start, self.stop = map(int, section.split("-"))


def is_valid(x: str) -> bool:
    return x[: len(x) // 2] == x[len(x) // 2 :]


def is_really_valid(x: str) -> bool:
    return any(x == (x[:i] * (len(x) // i))[: len(x)] for i in range(1, len(x) // 2 + 1))


class day1(riddle):
    def __init__(self, day, mode):
        super().__init__(day, mode)

    def a(self, function=is_valid):
        all_codes = [code(line) for line in self.lines[0].split(",")]
        print(
            sum(
                [
                    sum([x for x in range(c.start, c.stop + 1) if function(str(x))])
                    for c in all_codes
                ],
            ),
        )

    def b(self):
        self.a(function=is_really_valid)


if __name__ == "__main__":
    x = day1(day=2, mode="full")
    x.a()
    x.b()
