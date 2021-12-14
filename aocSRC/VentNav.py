# ======= Advent of Code ======= #
from typing import Any, Union, Dict
from SantasHelpers import get_input

def get_input(input_file, day=5):
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


class VentNav:
    def __init__(self, input=5) -> None:
        # self.input_file = r'Data/Day5.in'
        self.input_file = r'Data/test.in' 
        self.coordinates = get_input(self.input_file, input)

    def h_v_check(self, coords: list[list[int]]) -> list[bool, int]:
        non_diag = False
        x_y = None
        if coords[0][0] == coords[1][0]:
            non_diag = True
            x_y = 1
        if coords[0][1] == coords[1][1]:
            non_diag = True
            x_y = 0
        return non_diag, x_y

    def coordinate_marker(self, coordinates) -> None:
        # coords: [[1,2], [1,4]]
        non_diag, x_y = self.h_v_check(coordinates)
        if non_diag:
            for i in range(coordiates):
                pass
        print(non_diag, x_y)


    def part_one(self) -> int: # Part 2
        """loop through the coordinates and check them"""
        for i in range(len(self.coordinates)):
            self.coordinate_marker(self.coordinates[i])




    def part_two(self) -> None:
        return 

a = VentNav()
a.part_one()

def most_common(lst):
    counts = {}
    for i in lst:
        counts[i] = counts.get(i, 0) + 1
    return max(counts, key=counts.get)

