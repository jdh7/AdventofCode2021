# ======= Advent of Code ======= #
from typing import Any, Union, Dict
from SantasHelpers import get_input
from collections import Counter


class Coordinate:
    def __init__(self, coords) -> None:
        self.coords = coords
        self.all_points = None
        self.diagonal = True
        self.find_all_points()

    def find_all_points(self) -> list[int]:
        # [[1,2],[2,2]]
        all_points = set()
        x_min, y_min = [min(i) for i in zip(*self.coords)]
        x_max, y_max = [max(i) for i in zip(*self.coords)]
        if (x_min == x_max) or (y_min == y_max):
            self.diagonal = False
            for i in range(x_min, x_max+1):
                for j in range(y_min, y_max+1):
                    _x = (i, j)
                    all_points.add(_x)

        if (x_min != x_max) and (y_min != y_max):
            x_1, x_2 = [self.coords[x][0] for x in range(2)]
            y_1, y_2 = [self.coords[x][1] for x in range(2)]
            x_slope = 1 if (x_1 < x_2) else -1
            y_slope = 1 if (y_1 < y_2) else -1
            moves = abs(x_1 - x_2)

            for i in range(moves+1):
                _x = (x_1, y_1)
                all_points.add(_x)
                x_1 += x_slope
                y_1 += y_slope

        self.all_points = all_points
        return self.all_points


class VentNav:
    def __init__(self, input=5) -> None:
        # self.input_file = r'Data/Day5.in'
        self.input_file = r'Data/test.in'
        self.coordinate_list = get_input(self.input_file, input)
        self.build_coords()

    def build_coords(self) -> None:
        for ind, coords in enumerate(self.coordinate_list):
            self.coordinate_list[ind] = Coordinate(coords)

    def part_one(self) -> int:  # Part 2
        lst = []
        for i in self.coordinate_list:
            if not i.diagonal:
                lst.extend(_ for _ in i.all_points)

        # self.draw_board(lst)
        a = dict(Counter(lst))
        return sum(x >= 2 for x in a.values())

    def part_two(self) -> None:
        lst = []
        for i in self.coordinate_list:
            lst.extend(_ for _ in i.all_points)

        a = dict(Counter(lst))
        # self.draw_board(lst)
        return sum(x >= 2 for x in a.values())

    @staticmethod
    def draw_board(x):
        board = [[0 for _ in range(10)] for _ in range(10)]
        for i in x:
            r = i[1]
            c = i[0]
            board[r][c] += 1
        for i in board:
            print(i)
