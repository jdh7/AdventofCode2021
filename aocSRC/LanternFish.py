# ======= Advent of Code ======= #
from typing import Any, Union, Dict
from SantasHelpers import get_input
from collections import Counter


class Fish_counter:
    def __init__(self):
        self.input_file = r'Data/Day6.in'
#         self.input_file = r'Data/test.in'
        self.starting_fish = get_input(self.input_file, day=6)
        self.counts = self.initialize_counts(self.starting_fish)

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

    def initialize_counts(self, fish):
        counts = [0 for i in range(9)]
        for i in fish:
            counts[i] += 1
        return counts

    def cycle_fish(self):
        new_count = [self.counts[i] for i in [1, 2, 3, 4, 5, 6, 7, 8, 0]]
        new_count[6] += new_count[8]
        # print(new_count)
        # print(sum(new_count))
        self.counts = [i for i in new_count]

    def part_one(self, cycles=80):
        for i in range(cycles):
            self.cycle_fish()
        return sum(self.counts)

    def part_two(self, cycles=256):
        for i in range(cycles):
            self.cycle_fish()
        return sum(self.counts)
