# ======= Advent of Code ======= #
from typing import Any, Union, Dict
from SantasHelpers import get_input
from collections import Counter
import time

def get_input(input_file, day=5) -> list[list[int]]:
    # [[1,9],[2,9]]
    if day == 5:
        with open(input_file, 'r') as f:
            df = []
            for line in f.readlines():
                entry = []
                line = line.strip().split('->')
                for i in range(2):
                    coords = list(map(int, line[i].strip().split(',')))
                    entry.append(coords)
                df.append(entry)
        return df

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
                print(f'_x: {_x}')
                all_points.add(_x)

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

    def part_one(self) -> int: # Part 2
        lst = []
        for i in self.coordinate_list:
            if not i.diagonal:
                print(i.all_points)
                print('\n')
                lst.extend(_ for _ in i.all_points)
            print(lst)
            time.sleep(3)

        a = dict(Counter(lst))
        print(a, type(a))
        print(sum(x >= 2 for x in a.values()))


        return Counter(lst)

    def part_two(self) -> None:
        return 

a = VentNav()
a.part_one()


