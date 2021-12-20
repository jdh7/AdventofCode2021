# ======= Advent of Code ======= #

from typing import Any, Union, Dict
# from SantasHelpers import get_input
from collections import Counter

input_file = r'Data/test.in'
def get_input(input_file, day=9):
    if day == 9:
        with open(input_file, 'r') as f:
            df = []
            for line in f.readlines():
                entry = []
                line = line.strip()
                for c in line:
                    entry.append(int(c))
                df.append(entry)
        return df


class Lava_tubes: 
    def __init__(self, input=9) -> None:
        self.input_file = r'Data/Day9.in'
        # self.input_file = r'Data/test.in'
        self.x = get_input(self.input_file, input)
        # print(self.x)


    def part_one(self) -> int:  # Part 2
        lows = []
        # top adj: index -1, ind
        # leftadj: index, ind - 1
        # r___adj: index, ind + 1
        # bot_adj: index +1, ind
        # has top adj: index != 0
        # has leftadj: ind != 0
        # has r___adj: ind != len(e)
        # has bot_adj: index != len(self.x)

        for index, e in enumerate(self.x):
            for ind, j in enumerate(e):
                print(f'index: {index}, e: {e} \nind: {ind}, j: {j} ')
                low = True
                # check top
                if index != 0:
                    if self.x[index-1][ind] > j:
                        pass
                    else:
                        low = False
                # check left
                if ind != 0:
                    if self.x[index][ind-1] > j:
                        pass
                    else:
                        low = False
                # check right
                if ind != len(e)-1:
                    if self.x[index][ind+1] > j:
                        pass
                    else:
                        low = False
                # check bot
                if index != len(self.x)-1:
                    print(self.x[index+1][ind])
                    if self.x[index+1][ind] > j:
                        pass
                    else:
                        low = False
                if low == True:
                    lows.append(j)
                print(f'low: {low}')
                print(f'lows: {lows}')

        answer = [i+1 for i in lows]
        answer = sum(answer)
        print(answer)
        return answer

    def part_two(self) -> None:
        return


a = Lava_tubes()
a.part_one()

















        
    # def run_day(self, part=0):
        # answers = []
        # a = [self.part_one(),
        #     self.part_two()]
        # if part == 0:
        #     answers.append(a[0])
        #     answers.append(a[1])
        # else:
        #     answers.append(a[part])
        # for i in answers:
        #     yield i
