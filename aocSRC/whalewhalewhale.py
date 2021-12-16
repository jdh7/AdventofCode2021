# ======= Advent of Code ======= #

from typing import Any, Union, Dict
# from SantasHelpers import get_input
from collections import Counter, OrderedDict

def get_input(input_file, day=7):
    if day == 7:
        with open(input_file, 'r') as f:
            for line in f.readlines():
                line = [int(i) for i in line.split(',')]
    return line



class Puzzle_class:
    def __init__(self, day=7) -> None:
        self.input_file = r'Data/Day7.in'
        # self.input_file = r'Data/test.in'

        # [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
        self.crab_positions = get_input(self.input_file, day)

    def part_one(self) -> int:  # Part 2
        all_distances = OrderedDict()
        distances = [[] for i in range(len(self.crab_positions))]
        max_pos = max(self.crab_positions)
        for i in range(max_pos):
            for index, j in enumerate(self.crab_positions):
                distances[index] = abs(i - j)
            sum_distances = sum(distances)
            all_distances[sum_distances] = distances
            distances = [[] for i in range(len(self.crab_positions))]

        for k,v in sorted(all_distances.items()):
            print(k)

    def part_two(self) -> None:
        return

a = Puzzle_class()
a.part_one()






    # def run_day(self, part=0):
    #     answers = []
    #     a = [self.part_one(),
    #         self.part_two()]
    #     if part == 0:
    #         answers.append(a[0])
    #         answers.append(a[1])
    #     else:
    #         answers.append(a[part])
    #     for i in answers:
    #         yield i
