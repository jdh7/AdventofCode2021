# ======= Advent of Code ======= #

from typing import Any, Union, Dict
# from SantasHelpers import get_input
from collections import Counter
from dataclasses import dataclass


input_file = r'Data/test.in'
def get_input(input_file, day=8):
    if day == 8:
        with open(input_file, 'r') as f:
            signal_patterns = []
            output_values = []
            for line in f.readlines():
                x, y = line.split('|')
                x = x.split()
                y = y.split()
                signal_patterns.append(x)
                output_values.append(y)
        return signal_patterns, output_values


@dataclass
class Screen:
    has_side = {
        # 0 : [1,1,1,0,1,1,1],      # 6
        1 : [0,0,1,0,0,1,0],        # 2

        # 2 : [1,0,1,1,1,0,1],      # 5
        # 3 : [1,0,1,1,0,1,1],      # 5
        4 : [0,1,1,1,0,1,0],        # 4
        # 5 : [1,1,0,1,0,1,1],      # 5

        # 6 : [1,1,0,1,1,1,1],      # 6
        7 : [1,0,1,0,0,1,0],        # 3
        8 : [1,1,1,1,1,1,1],        # 7
        # 9 : [1,1,1,1,0,1,1]       # 6
    }


class Part_One:
    def __init__(self, input=8) -> None:
        # self.input_file = r'Data/Day8.in'
        self.input_file = r'Data/test.in'
        self.signal_patterns, self.output_values = get_input(self.input_file, input)

    def part_two(self):
        for i in self.signal_patterns:
            print(i)
            self.map_wires(i)
            exit(0)

    def map_wires(self, scrambled_display):
        wire_map = {
            'T': set(),
            'TL': set(),
            'TR': set(),
            'M': set(),
            'BL': set(),
            'BR': set(),
            'B': set()
        }
        scrambled_display.sort(key=len)
        # print(scrambled_display)
        two_len = dict(Counter(scrambled_display[0]))
        three_len = dict(Counter(scrambled_display[1]))
        four_len = dict(Counter(scrambled_display[2]))
        stringplus = ""
        for i in scrambled_display[3:6]:
            stringplus += i
        five_len = dict(Counter(stringplus))
        stringplus = ""
        for i in scrambled_display[6:9]:
            stringplus += i
        six_len = dict(Counter(stringplus))
        sev_len = dict(Counter(scrambled_display[8]))
        def find_wires():
            for i in "abcdefg":
                #Top
                if (i not in two_len) and (i in sev_len) and (i not in
    four_len) and (five_len[i] == 3) and (six_len[i] == 3):
                    wire_map['T'] = i
                #TopLeft
                if (i not in two_len) and (i in three_len) and (i in four_len) and (five_len[i] == 1) and (six_len[i] == 3):
                    wire_map['TL'] = i
                #TopRight
                if (i in two_len) and (i in three_len) and (i in four_len) and (five_len[i] == 2) and (six_len[i] == 2):
                    wire_map['TR'] = i
                #MID
                if (i not in two_len) and (i not in three_len) and (i in four_len) and (five_len[i] == 3) and (six_len[i] == 2):
                    wire_map['M'] = i
                #BotLeft
                if (i not in two_len) and (i not in three_len) and (i not in four_len) and (five_len[i] == 1) and (six_len[i] == 2):
                    wire_map['BL'] = i
                #BotRight
                if (i in two_len) and (i in three_len) and (i in four_len) and (five_len[i] == 2) and (six_len[i] == 3):
                    wire_map['BR'] = i
                #BOT
                if (i not in two_len) and (i not in three_len) and (i not in four_len) and (five_len[i] == 3) and (six_len[i] == 3):
                    wire_map['B'] = i




        has_side = {
            1 : [0,0,1,0,0,1,0],        # 2
            7 : [1,0,1,0,0,1,0],        # 3
            4 : [0,1,1,1,0,1,0],        # 4

          # 2 : [1,0,1,1,1,0,1],      # 5
          # 3 : [1,0,1,1,0,1,1],      # 5
          # 5 : [1,1,0,1,0,1,1],      # 5

          # 0 : [1,1,1,0,1,1,1],      # 6
          # 6 : [1,1,0,1,1,1,1],      # 6
          # 9 : [1,1,1,1,0,1,1]       # 6

            8 : [1,1,1,1,1,1,1]        # 7
        }

        



a = Part_One()
a.part_two()
