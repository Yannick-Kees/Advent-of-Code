# SPDX-FileCopyrightText: 2025 Yannick Kees
#
# SPDX-License-Identifier: MIT


from src.base_class import riddle

TOTAL_SIZE = 100
START_POINT = 50


class day1(riddle):
    def __init__(self, day, mode):
        super().__init__(day, mode)

    def a(self):
        pass


if __name__ == "__main__":
    x = day1(day=2, mode="test")
    x.a()
