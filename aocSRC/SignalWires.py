# ======= Advent of Code ======= #

from typing import Any, Union, Dict
# from SantasHelpers import get_input
from collections import Counter
from dataclasses import dataclass


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

class Part_One:
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
        return  sum([value for key,value in count.items() if key in [2,3,4,7]]) 

"""   
     1:      4:      7:       8:
  ....    ....    aaaa     aaaa
 .    c  b    c  .    c   b    c
 .    c  b    c  .    c   b    c
  ....    dddd    ....     dddd
 .    f  .    f  .    f   e    f
 .    f  .    f  .    f   e    f
  ....    ....    ....     gggg

 0:       2:      3:
 aaaa     aaaa    aaaa 
b    c   .    c  .    c
b    c   .    c  .    c
 ....     dddd    dddd 
e    f   e    .  .    f
e    f   e    .  .    f
 gggg     gggg    gggg 

  5:       6:       9:
 aaaa     aaaa     aaaa
b    .   b    .   b    c
b    .   b    .   b    c
 dddd     dddd     dddd
.    f   e    f   .    f
.    f   e    f   .    f
 gggg     gggg     gggg

"""

@dataclass
class Screen:
    code: str
    length: int = None
    sides: list[int] = None
    potential_digits: list[int] = None
    true_digit: int = None 
    potential_sides = [] 

    def set_length(self):
        self.length = len(self.code)
        lengths = {2:1,4:4,3:7,7:8}
        for k,v in lengths.items():
            if self.length == k:
                self.true_digit = v

    def set_poss_digs(self):
        if len(self.code) == 5:
            self.potential_digits = [2,3,5]
        if len(self.code) == 6:
            self.potential_digits = [0,6,9]
    

class Decoder:
    def __init__(self) -> None:
        self.input_file = r'Data/test.in'
        self.all_inputs: list[list[str]] =  get_input(self.input_file) 
        pass 

        self.has_side = {
            1 : [0,0,1,0,0,1,0],
            7 : [1,0,1,0,0,1,0],
            4 : [0,1,1,1,0,1,0],

            2 : [1,0,1,1,1,0,1],
            3 : [1,0,1,1,0,1,1],
            5 : [1,1,0,1,0,1,1],

            0 : [1,1,1,0,1,1,1],
            6 : [1,1,0,1,1,1,1],
            9 : [1,1,1,1,0,1,1],

            8 : [1,1,1,1,1,1,1]
        }

    def create_screens(self):
        for i in self.all_inputs:
            for index, e in enumerate(i):
                i[index] = Screen(e)
                i[index].set_length()
                i[index].potential_sides.append(self.has_side[i[index].length])
                # i.potential_sides.append(self.has_side[i.length])
            
    def part_2(self):
        self.create_screens()
        for i in self.all_inputs:
            print(i)
            self.potential_numbers(i)
            break
    
    def potential_numbers(self, scrambled_display):
        # Get all the true digits
        true_digits: list[list[int]] = [] 
        for index, e in enumerate(scrambled_display):
            if e.true_digit != None: 
                true_digits.append([e.true_digit, index])

        # build a potential side map         
        potential_sides = [
            [['T'], set()],
            [['TL'], set()],
            [['TR'], set()],
            [['M'], set()],
            [['BL'], set()],
            [['BR'], set()],
            [['B'], set()]
    ] 

        #find out what sides the true_digits have in common
        common_sides = [0 for _ in range(7)]
        lst_to_check = []
        for i in true_digits:
            x = i[0]
            lst_to_check.append(self.has_side[x])

        lst_to_check = [
            int(sum(i) == len(lst_to_check))
            for i in zip(*lst_to_check)
    ] 
        print(lst_to_check)

        #find out what wires we have in common
        common_wires = []
        for i in true_digits:
            print(i)
            common_wires.append(scrambled_display[i[1]].code)

        common_wires = [set(x) for x in common_wires]
        common_wires = set[0].intersection(*common_wires)
        print(common_wires)

        #set the potential side wires for common sides 
        for index, e in enumerate(lst_to_check):
            if e:
                potential_sides[index][1].update(x for x in common_wires)

        #find the sides we don't have in common
        uncommon_sides = [0 for _ in range(7)]
        second_lst_to_check = []
        for i in true_digits:
            x = i[0]
            second_lst_to_check.append(self.has_side[x])

        second_lst_to_check = [
            int(sum(i) != len(second_lst_to_check))
            for i in zip(*second_lst_to_check)
    ] 
        print(second_lst_to_check)

        #find the wires we dont have in common
        
        
        
                




    def decode(self, scrambled_display):
        # I have all the unique numbers already in the dataclass 
        # What I have to do is determine potential numbers


        pass
    
a = Decoder()
a.part_2()







class Decoder_RAW:
    def __init__(self, scrambled_display: list[list[str]] = None):
        #{top 0, left 1, right 2, mid 3, left 4, right 5, bot 6}
        self.answers = dict()
        self.scrambled_display = scrambled_display
        self.map_of_digits = {
            "top": "a",
            "top_l": "b",
            "top_r": "c",
            "mid": "d",
            "bot_l": "e",
            "bot_r": "f",
            "bot": "g"
    }
        self.has_side = {
            0 : [1,1,1,0,1,1,1],
            1 : [0,0,1,0,0,1,0],
            2 : [1,0,1,1,1,0,1],
            3 : [1,0,1,1,0,1,1],
            4 : [0,1,1,1,0,1,0],
            5 : [1,1,0,1,0,1,1],
            6 : [1,1,0,1,1,1,1],
            7 : [1,0,1,0,0,1,0],
            8 : [1,1,1,1,1,1,1],
            9 : [1,1,1,1,0,1,1]
        }
        self.create_screens()

    def create_screens(self):
        for i,e in enumerate(self.scrambled_display):
            self.scrambled_display[i] = Screen(e)
            self.scrambled_display[i].set_length()
        print(self.scrambled_display)


        

    def draw_digit(self):
        print("\n")
        print(" "+self.map_of_digits["top"]*4+" ")
        print(self.map_of_digits["top_l"]+"    "+self.map_of_digits["top_r"])
        print(self.map_of_digits["top_l"]+"    "+self.map_of_digits["top_r"])
        print(" "+self.map_of_digits["mid"]*4+" ")
        print(self.map_of_digits["bot_l"]+"    "+self.map_of_digits["bot_r"])
        print(self.map_of_digits["bot_l"]+"    "+self.map_of_digits["bot_r"])
        print(" "+self.map_of_digits["bot"]*4+" ")
        print("\n")







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

