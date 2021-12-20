# ======= Advent of Code ======= #

from typing import Any, Union, Dict
from SantasHelpers import get_input
from collections import Counter

class Wire_decoder:
    def __init__(self, input=8) -> None:
        self.input_file = r'Data/Day8.in'
        # self.input_file = r'Data/test.in'
        self.signal_patterns, self.output_values = get_input(
            self.input_file, input)

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

    def part_one(self):
        count = 0
        for i in self.output_values:
            for j in i:
                x = [2,3,4,7]
                if len(j) in x:
                    count += 1
        return count

    def part_two(self):
        answer = 0
        for i, j in zip(self.signal_patterns, self.output_values):
            i_wire_map = self.map_wires(i)
            answer += self.decode_output(j, i_wire_map)
        return(answer)

    def decode_output(self, output_value, wire_map):
        code = []
        for i in output_value:
            x = {2:1, 3:7, 4:4, 7:8}
            if len(i) in x:
                code.append(x[len(i)])
            elif len(i) == 5:
                if wire_map['TL'] in i:
                    code.append(5)
                if wire_map['BL'] in i:
                    code.append(2)
                if (wire_map['TL'] not in i) and (wire_map['BL'] not in i):
                    code.append(3)
            elif len(i) == 6:
                if wire_map['M'] not in i:
                    code.append(0)
                if wire_map['TR'] not in i:
                    code.append(6)
                if (wire_map['BL'] not in i) and (wire_map['BL'] not in i):
                    code.append(9)
        int_code = ""
        for i in code:
            int_code += str(i)

        return(int(int_code))

    def map_wires(self, scrambled_display):
        wire_map = {
            'T': None,
            'TL': None,
            'TR': None,
            'M': None,
            'BL': None,
            'BR': None,
            'B': None
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

        def find_wires():
            for i in "abcdefg":
                # Top
                if (i not in two_len) \
                    and (i in three_len) \
                    and (i not in four_len) \
                    and (five_len[i] == 3) \
                    and (six_len[i] == 3):
                    wire_map['T'] = i
                # TopLeft
                if (i not in two_len) \
                    and (i not in three_len) \
                    and (i in four_len) \
                    and (five_len[i] == 1) \
                    and (six_len[i] == 3):
                    wire_map['TL'] = i
                # TopRight
                if (i in two_len) \
                    and (i in three_len) \
                    and (i in four_len) \
                    and (five_len[i] == 2) \
                    and (six_len[i] == 2):
                    wire_map['TR'] = i
                # MID
                if (i not in two_len) \
                    and (i not in three_len) \
                    and (i in four_len) \
                    and (five_len[i] == 3) \
                    and (six_len[i] == 2):
                    wire_map['M'] = i
                # BotLeft
                if (i not in two_len) \
                    and (i not in three_len) \
                    and (i not in four_len) \
                    and (five_len[i] == 1) \
                    and (six_len[i] == 2):
                    wire_map['BL'] = i
                # BotRight
                if (i in two_len) \
                    and (i in three_len) \
                    and (i in four_len) \
                    and (five_len[i] == 2) \
                    and (six_len[i] == 3):
                    wire_map['BR'] = i
                # BOT
                if (i not in two_len) \
                    and (i not in three_len) \
                    and (i not in four_len) \
                    and (five_len[i] == 3) \
                    and (six_len[i] == 3):
                    wire_map['B'] = i

            # find remainder letter in case
            remainder = ""
            for i in "abcdefg":
                if i not in wire_map.values():
                    remainder = i
                    
            for k,v in wire_map.items():
                if v == None:
                    wire_map[k] = remainder

            return wire_map



        wire_map = find_wires()
        return wire_map

a = Wire_decoder()
print(a.part_one())
