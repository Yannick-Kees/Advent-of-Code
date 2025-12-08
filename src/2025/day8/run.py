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
    def __init__(self):
        self.connections = []

    def add_connection(self, junction: Point):
        self.connections.append(junction)

    def get_length(self):
        return len(self.connections)

    def __add__(self, other):
        new_circuit = circuit()
        new_circuit.connections = self.connections + other.connections
        return new_circuit


class day(riddle):
    def __init__(self, day, mode):
        super().__init__(day, mode)
        points = [Point(line) for line in self.lines]

        self.lookup_table = {}
        for p in points:
            c = circuit()
            c.add_connection(p)
            self.lookup_table[p] = c

        distances = [
            (p1, p2, p1 - p2) for i, p1 in enumerate(points) for j, p2 in enumerate(points) if i < j
        ]
        self.distances = sorted(distances, key=lambda x: x[2])

    def a(self):
        for p1, p2, _ in self.distances[:1000]:
            if self.lookup_table[p1] is not self.lookup_table[p2]:
                new_ciruit = self.lookup_table[p1] + self.lookup_table[p2]
                for p in new_ciruit.connections:
                    self.lookup_table[p] = new_ciruit

        unique_circuits = set()
        for c in self.lookup_table.values():
            unique_circuits.add(c.get_length())

        r = sorted(unique_circuits)
        print(r[-1] * r[-2] * r[-3])

    def b(self):
        for p1, p2, _ in self.distances:
            if self.lookup_table[p1] is not self.lookup_table[p2]:
                new_ciruit = self.lookup_table[p1] + self.lookup_table[p2]
                for p in new_ciruit.connections:
                    self.lookup_table[p] = new_ciruit

                unique_circuits = set()
                for c in self.lookup_table.values():
                    unique_circuits.add(id(c))
                if len(unique_circuits) == 1:
                    print(p1.x * p2.x)
                    break


if __name__ == "__main__":
    x = day(day=8, mode="full")
    x.a()
    x.b()

#
#  117000
# 8368033065 b
