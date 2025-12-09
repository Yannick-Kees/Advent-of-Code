# SPDX-FileCopyrightText: 2025 Yannick Kees
#
# SPDX-License-Identifier: MIT


from src.base_class import riddle


class Point:
    def __init__(self, line):
        self.x, self.y, self.z = list(map(int, line.replace("\n", "").split(",")))

    def __sub__(self, other):
        return abs(self.x - other.x) ** 2 + abs(self.y - other.y) ** 2 + abs(self.z - other.z) ** 2


class circuit:
    def __init__(self, points: list[Point]):
        self.connections = points

    def __add__(self, other):
        return circuit(self.connections + other.connections)


class day(riddle):
    def __init__(self, day, mode):
        super().__init__(day, mode)
        self.points = [Point(line) for line in self.lines]
        distances = [
            (p1, p2, p1 - p2)
            for i, p1 in enumerate(self.points)
            for j, p2 in enumerate(self.points)
            if i < j
        ]
        self.distances = sorted(distances, key=lambda x: x[2])

    def clear_look_up_table(self):
        self.lookup_table = {p: circuit([p]) for p in self.points}

    def create_circuits(self, upper_bound: int = None):
        self.clear_look_up_table()
        for p1, p2, _ in self.distances[:upper_bound] if upper_bound else self.distances:
            if self.lookup_table[p1] is not self.lookup_table[p2]:
                new_ciruit = self.lookup_table[p1] + self.lookup_table[p2]
                for p in new_ciruit.connections:
                    self.lookup_table[p] = new_ciruit

                unique_circuits = {id(c) for c in self.lookup_table.values()}
                
                if len(unique_circuits) == 1:
                    print(p1.x * p2.x)
                    break

    def a(self):
        self.create_circuits(upper_bound=1000)
        unique_circuits = sorted({len(c.connections) for c in self.lookup_table.values()})
        print(unique_circuits[-1] * unique_circuits[-2] * unique_circuits[-3])

    def b(self):
        self.create_circuits()


if __name__ == "__main__":
    x = day(day=8, mode="full")
    x.a()
    x.b()

#  117000
# 8368033065 b
