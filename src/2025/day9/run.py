# SPDX-FileCopyrightText: 2025 Yannick Kees
#
# SPDX-License-Identifier: MIT

from src.base_class import riddle


class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"


class Point:
    def __init__(self, line: str):
        x, y = [int(i) for i in line.split(",")]
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Rectangle(abs(self.x - other.x) + 1, abs(self.y - other.y) + 1)


class day(riddle):
    def __init__(self, day, mode):
        super().__init__(day, mode)
        self.points = [Point(line) for line in self.lines]

    def a(self):
        area = 0
        for x in self.points:
            for y in self.points:
                new_area = (x + y).area()
                if new_area > area:
                    area = new_area

        print(area)

    def b(self):
        pass


if __name__ == "__main__":
    x = day(day=9, mode="full")
    x.a()
    x.b()
