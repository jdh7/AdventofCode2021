# ======= Advent of Code ======= #

from typing import Any, Union, Dict
# from SantasHelpers import get_input
from collections import Counter

input_file = 'Data/Day6.in'
def get_input(input_file, day=6):
    if day == 6:
        with open(input_file, 'r') as f:
            for line in f.readlines():
                line = [int(i) for i in line.split(',')]
    return line


class Fish_counter:
    def __init__(self, starting_fish):
        self.counts = self.initialize_counts(starting_fish)

    def initialize_counts(self, fish):
        counts = [0 for i in range(9)]
        for i in fish:
            counts[i] += 1
        return counts

    def cycle_fish(self):
        new_count = [self.counts[i] for i in [1,2,3,4,5,6,7,8,0]]
        new_count[6] += new_count[8]
        print(new_count)
        print(sum(new_count))
        self.counts = [i for i in new_count]



    def part_one(self, cycles):
        for i in range(cycles):
            self.cycle_fish()
        return sum(self.counts)


fish = get_input(input_file)
print(fish)
a = Fish_counter(fish)
a.part_one(256)

        



















# @dataclass
# class LanternFish:
#     first_spawn: bool
#     days_to_first_spawn: int = 8
#     days_to_spawn: int = 6

# class Puzzle_class:
#     def __init__(self, input=X) -> None:
#         self.input_file = r'Data/DayX.in'
#         self.input_file = r'Data/test.in'
#         self.x = get_input(self.input_file, input)

#     # def run_day(self, part=0):
#     #     answers = []
#     #     a = [self.part_one(),
#     #         self.part_two()]
#     #     if part == 0:
#     #         answers.append(a[0])
#     #         answers.append(a[1])
#     #     else:
#     #         answers.append(a[part])
#     #     for i in answers:
#     #         yield i

#     def part_one(self) -> int:  # Part 2
#         return

#     def part_two(self) -> None:
#         return

# a = Puzzle_class()
# print(a.part_one)
# print(a.part_two)
