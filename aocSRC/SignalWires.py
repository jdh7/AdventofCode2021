# ======= Advent of Code ======= #

from typing import Any, Union, Dict
# from SantasHelpers import get_input
from collections import Counter

one = "cf"       #2
seven = "acf"    #3
four = "bcdf"    #4

two = "acdeg"    #5
three = "acdfg"  #5
five = "abdfg"   #5

six = "abdefg"   #6
zero = "abcefg"  #6
nine = "abcdfg"  #6

eight = "abcdefg"#7


input_file = r'Data/test.in'
def get_input(input_file, day=8):
    if day == 8:
        with open(input_file, 'r') as f:
            output_values = []
            for line in f.readlines():
                x, y = line.split('|')
                y = y.split()
                output_values.append(y)
        return output_values
get_input(input_file)


class Puzzle_class:
    def __init__(self, input=8) -> None:
        self.input_file = r'Data/Day8.in'
        # self.input_file = r'Data/test.in'
        self.x = get_input(self.input_file, input)

    def part_one(self) -> int:  
        count = dict()
        for i in self.x:
            for j in i:
                l = len(j)
                if l not in count:
                    count[l]=1
                else:
                    count[l] += 1
        print(count)
        return  sum([value for key,value in count.items() if key in [2,3,4,7]]) 

    def part_two(self) -> None:
        return

a = Puzzle_class()
print(a.part_one())




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
