# ======= Advent of Code ======= #
from typing import Any, Union, Dict
from SantasHelpers import get_input

# Suffering from too bad a headcold to write this any better
class SquidBingo:
    def __init__(self, input=4) -> None:
        self.input_file = r'Data/Day4.in'
        # self.input_file = r'Data/test.in' 
        self.moves, self.boards = get_input(self.input_file, input)

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

    def check_sum(self, x: list[list[int]]) -> bool:
        solved = False
        a = [sum(i) for i in zip(*x)]
        if 5 in a:
            solved = True
        b = [sum(i) for i in x]
        if 5 in b:
            solved = True
        return solved

    def board_marker(self, i: int) -> Union[int, list]: 
        for n in range(len(self.moves)):
            for j in range(len(self.boards[0])):
                for c in range(len(self.boards[0][0])):
                    if self.boards[i][j][c] == self.moves[n]:
                        self.marked_numbers[j][c] = 1
                        if self.check_sum(self.marked_numbers)==True:
                            x = [i for i in self.marked_numbers]
                            return n, i, x, self.moves[n] 

    def part_one(self) -> int: # Part 2
        winning_board_info = [2001, 0, 0, 0]

        # check all boards for their time to win
        for i in range(len(self.boards)):
            self.marked_numbers = [[0 for _ in range(5)] for _ in range(5)]
            _n, _i, _marked, _m = self.board_marker(i)
            if _n < winning_board_info[0]:
                winning_board_info[0] = _n
                winning_board_info[1] = _i
                winning_board_info[2] = _marked
                winning_board_info[3] = _m

        winning_board = winning_board_info[2]
        winning_board_marked = winning_board_info[0]
        winning_board_index = winning_board_info[1]
        winning_move = winning_board_info[3]

        # calculate sum of all non-marked numbers
        total_score = 0
        for i in range(len(winning_board)):
            for j in range(len(winning_board[0])):
                if (winning_board[i][j]) == 0:
                    total_score += self.boards[winning_board_index][i][j]

        # print(f'total_score: {total_score}')
        # print(f'winning_move: {winning_move}')
        return total_score*winning_move

    def part_two(self) -> None:
        winning_board_info = [0, 0, 0, 0]

        # check all boards for their time to win
        for i in range(len(self.boards)):
            self.marked_numbers = [[0 for _ in range(5)] for _ in range(5)]
            _n, _i, _marked, _m = self.board_marker(i)
            if _n > winning_board_info[0]:
                winning_board_info[0] = _n
                winning_board_info[1] = _i
                winning_board_info[2] = _marked
                winning_board_info[3] = _m

        winning_board = winning_board_info[2]
        winning_board_marked = winning_board_info[0]
        winning_board_index = winning_board_info[1]
        winning_move = winning_board_info[3]

        # calculate sum of all non-marked numbers
        total_score = 0
        for i in range(len(winning_board)):
            for j in range(len(winning_board[0])):
                if (winning_board[i][j]) == 0:
                    total_score += self.boards[winning_board_index][i][j]

        # print(f'total_score: {total_score}')
        # print(f'winning_move: {winning_move}')
        return total_score*winning_move
