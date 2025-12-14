# SPDX-FileCopyrightText: 2025 Yannick Kees
#
# SPDX-License-Identifier: MIT

from src.base_class import riddle


class day(riddle):
    def __init__(self, day, mode):
        super().__init__(day, mode)

    def a(self):
        pass

    def b(self):
        pass


if __name__ == "__main__":
    x = day(day=8, mode="full")
    x.a()
    x.b()
