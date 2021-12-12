# ======= Advent of Code ======= #
from typing import Any, Union, Dict
from SantasHelpers import bin_to_dec, most_common_digit #, get_input

input_file = r'Data/test.in'
def get_input(input_file, input):
    x = []
    entry = []
    if input == 4:
        with open(input_file, 'r') as f:
            for line in f.readlines():
                line = line.strip().split()
                if not line:
                    x.append(entry)
                    entry = []
                else:
                    entry.append(line)
        x.append(entry)
    bingo_moves = x[0][0][0].split(',')
    bingo_moves = list(map(int, bingo_moves))

    boards = x[1:]
    for i in range(len(boards)):
        for j in range(len(boards[i])):
            boards[i][j] = list(map(int, boards[i][j]))


    return bingo_moves, boards

moves: list[int]
boards: list[list[int]]
# moves, boards = get_input(input_file, input = 4)

class SquidBingo:
    def __init__(self, input=4) -> None:
        # self.input_file = r'Data/test.in'
        self.input_file = r'Data/test.in' 
        self.moves, self.board = get_input(self.input_file, input)
        

    
    def part_one(self) -> int: # Part 2
        # Create a blank
        marked_numbers = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(len(self.board))] # numpy zeros
        return None

@dataclass
class Board:
    numbered_board: list[int]
    placed_board: list[int]



a = SquidBingo()
a.part_one()
