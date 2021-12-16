# ======= Advent of Code ======= #

from typing import Any, Union, Dict
from SantasHelpers import get_input
from collections import Counter, OrderedDict


class Crab_scooter:
    def __init__(self, day=7) -> None:
        self.input_file = r'Data/Day7.in'
        # self.input_file = r'Data/test.in'
        self.crab_positions = get_input(self.input_file, day)

    def run_day(self, part=0):
        answers = []
        a = [self.part_one(),
            self.part_two()]
        if part == 0:
            answers.append(a[0])
            answers.append(a[1])
        else:
            answers.append(a[part])
        for i in answers:
            yield i

    def part_one(self) -> int:  # Part 2
        # brute force best force
        all_distances = OrderedDict()
        distances = [[] for i in range(len(self.crab_positions))]
        max_pos = max(self.crab_positions)
        for i in range(max_pos):
            for index, j in enumerate(self.crab_positions):
                distances[index] = abs(i - j)
            sum_distances = sum(distances)
            all_distances[sum_distances] = distances
            distances = [[] for i in range(len(self.crab_positions))]

        return sorted(all_distances.keys())[0] 


    def part_two(self) -> None:
        all_distances = OrderedDict()
        distances = [[] for i in range(len(self.crab_positions))]
        max_pos = max(self.crab_positions)
        for i in range(max_pos):
            for index, j in enumerate(self.crab_positions):
                n = abs(i-j)
                distances[index] = int((n**2 + n)/2)
            sum_distances = sum(distances)
            all_distances[sum_distances] = distances
            distances = [[] for i in range(len(self.crab_positions))]

        return sorted(all_distances.keys())[0] 
