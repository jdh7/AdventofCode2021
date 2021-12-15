# ======= Advent of Code ======= #

from typing import Any, Union, Dict
# from SantasHelpers import get_input
from collections import Counter
from dataclasses import dataclass

RAW = """3,3,2,1,4,1,1,2,3,1,1,2,1,2,1,1,1,1,1,1,4,1,1,5,2,1,1,2,1,1,1,3,5,1,5,5,1,1,1,1,3,1,1,3,2,1,1,1,1,1,1,4,1,1,1,1,1,1,1,4,1,3,3,1,1,3,1,3,1,2,1,3,1,1,4,1,2,4,4,5,1,1,1,1,1,1,4,1,5,1,1,5,1,1,3,3,1,3,2,5,2,4,1,4,1,2,4,5,1,1,5,1,1,1,4,1,1,5,2,1,1,5,1,1,1,5,1,1,1,1,1,3,1,5,3,2,1,1,2,2,1,2,1,1,5,1,1,4,5,1,4,3,1,1,1,1,1,1,5,1,1,1,5,2,1,1,1,5,1,1,1,4,4,2,1,1,1,1,1,1,1,3,1,1,4,4,1,4,1,1,5,3,1,1,1,5,2,2,4,2,1,1,3,1,5,5,1,1,1,4,1,5,1,1,1,4,3,3,3,1,3,1,5,1,4,2,1,1,5,1,1,1,5,5,1,1,2,1,1,1,3,1,1,1,2,3,1,2,2,3,1,3,1,1,4,1,1,2,1,1,1,1,3,5,1,1,2,1,1,1,4,1,1,1,1,1,2,4,1,1,5,3,1,1,1,2,2,2,1,5,1,3,5,3,1,1,4,1,1,4"""

fish = [3,4,3,1,2]
# fish = [int(i) for i in RAW.split(',')]
def fishy_multiplier(cycles:int, fish: list[int]) -> int:
    for i in range(cycles):
        for i, e in enumerate(fish):
            # print(f'i: {i}, e: {e}')
            if e != 0:
                fish[i] -= 1
            if e == 0:
                fish.append(9)
                fish[i] = 6

        # print(fish)
        print(len(fish))

fishy_multiplier(256, fish)


# oh noooo, idk how to do this second part :(

















# def get_input(input_file, input=5):
#     if day == 4:
#         x = []
#         entry = []
#         with open(input_file, 'r') as f:
#             for line in f.readlines():
#                 line = line.strip().split()
#                 if not line:
#                     x.append(entry)
#                     entry = []
#                 else:
#                     entry.append(line)
#         x.append(entry)
#         bingo_moves = x[0][0][0].split(',')
#         bingo_moves = list(map(int, bingo_moves))

#         boards = x[1:]
#         for i in range(len(boards)):
#             for j in range(len(boards[i])):
#                 boards[i][j] = list(map(int, boards[i][j]))

#         return bingo_moves, boards

#     if day == 5:
#         with open(input_file, 'r') as f:
#             df = []
#             for line in f.readlines():
#                 entry = []
#                 line = line.strip().split('->')
#                 for i in range(2):
#                     coords = list(map(int, line[i].strip().split(',')))
#                     entry.append(coords)
#                 df.append(entry)
#         return df


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

