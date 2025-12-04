# SPDX-FileCopyrightText: 2025 Yannick Kees
#
# SPDX-License-Identifier: MIT


import numpy as np

from src.base_class import riddle

positions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]


def check_pos(matrix, current_pos):
    rolls = 0
    if matrix[current_pos[0]][current_pos[1]] == 1:
        for pos in positions:
            i, j = [pos[i] + current_pos[i] for i in range(2)]

            if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
                if matrix[i][j] == 1:
                    rolls += 1

        return 0 if rolls < 4 else 1
    return 0


class day(riddle):
    def __init__(self, day, mode):
        super().__init__(day, mode)

    def a(self, a: bool = True):
        matrix = np.array([[0 if char == "." else 1 for char in list(line)] for line in self.lines])
        paper = 0
        while True or a:
            new_matrix = np.array(
                [
                    [check_pos(matrix, [i, j]) for j in range(len(matrix[0]))]
                    for i in range(len(matrix))
                ],
            )
            removed = np.sum(matrix - new_matrix)
            paper += removed

            if removed == 0 or a:
                break

            matrix = new_matrix

        print(paper)

    def b(self):
        self.a(a=False)


if __name__ == "__main__":
    x = day(day=4, mode="full")
    x.a()  # 1518
    x.b()  # 8665
