# ======= Advent of Code ======= #
from typing import Any, Union, Dict
from SantasHelpers import bin_to_dec, get_input, most_common_digit


class LifeSupport: # Day 3
    def __init__(self, input=3) -> None:
        # self.input_file = r'Data/test.in'
        self.input_file = r'Data/Day3.in' 

        self.df = get_input(self.input_file, input)
    
    def run_day(self, part=0):
        answers = []
        a = [self.diagnostic_report(),
            self.life_support()]
        if part == 0:
            answers.append(a[0])
            answers.append(a[1])
        else:
            answers.append(a[part])

        for i in answers:
            yield i

    def diagnostic_report(self, x: Union[str, int] = None) -> int: # Part 1
        if x == None:
            x = self.df
        x: list[str]

        gamma_rate_bin = most_common_digit(x)
        epsilon_rate_bin = most_common_digit(x, choice=False)
        
        gamma_rate = bin_to_dec(gamma_rate_bin) 
        epsilon_rate = bin_to_dec(epsilon_rate_bin) 
        
        # print(f'The answer to part 1 is: {gamma_rate*epsilon_rate}')
        return gamma_rate*epsilon_rate
        

    def life_support(self, x: Union[str, int] = None) -> int: # Part 2
        if x == None:
            x = self.df

        self.check_nums = [i for i in x]
        self.keep_nums = []

        def find_nums(nums: list[str], run_count: int, choice = True) -> list[str]:
            a = most_common_digit(nums, choice=choice)
            
            for i in range(len(nums)):
                if nums[i][run_count] == a[run_count]:
                    self.keep_nums.append(nums[i])
            self.check_nums = [i for i in self.keep_nums]
            self.keep_nums.clear()

        run_count = 0
        while len(self.check_nums) > 1:
            find_nums(self.check_nums, run_count)
            run_count += 1

        OGR = bin_to_dec(self.check_nums)

        self.check_nums = [i for i in x]
        run_count = 0
        while len(self.check_nums) > 1:
            find_nums(self.check_nums, run_count, choice = False)
            run_count += 1

        C02 = bin_to_dec(self.check_nums)

        # print(f'The answer to part 2 is: {OGR*C02}')
        return OGR*C02



class Sub_driving: # Day 2
    def __init__(self, input=2) -> None:
        # self.input_file = r'Data/test.in'
        self.input_file = r'Data/Day2.in' 

        self.df = get_input(self.input_file, input)
    
    def run_day(self, part=0):
        answers = []
        a = [self.pilot_sub(),
            self.aim_pilot_sub()]

        if part == 0:
            answers.append(a[0])
            answers.append(a[1])
        else:
            answers.append(a[part])

        for i in answers:
            yield i

    def pilot_sub(self, x: Union[str, int] = None) -> int: # Part 1
        if x == None:
            x = self.df

        sub_position: list[int] = [0, 0]  # horizontal , depth
        sub_directions: Dict[str, list[int]] = {'up': [1, -1], 'down': [1, 1],
                                                'forward': [0, 1]}

        # i e.g. ['up', 5]
        for i in x:

            direction: str = i[0]
            distance: int = int(i[1])
            multiplier: int = sub_directions[direction][1]
            pos: int = sub_directions[direction][0]

            sub_position[pos] += distance * multiplier

        # print(f'The answer to part 1 is: {(sub_position[0]*sub_position[1])}')
        return (sub_position[0]*sub_position[1])

    def aim_pilot_sub(self, x: Union[str, int] = None) -> int: # Part 2
        if x == None:
            x = self.df

        sub_position: list[int] = [0, 0, 0]  # horizontal , depth, aim
        sub_directions: Dict[str, list[int]] = {'up': [2, -1], 'down': [2, 1],
                                                'forward': [0, 1]}

        for i in x:
            direction: str = i[0]
            amount: int = int(i[1])
            multiplier: int = sub_directions[direction][1]
            pos: int = sub_directions[direction][0]

            if direction != 'forward':
                sub_position[2] += amount * multiplier

            else:
                sub_position[0] += amount
                sub_position[1] += amount*sub_position[2]

        # print(f'The answer to part 1 is: {(sub_position[0]*sub_position[1])}')
        return (sub_position[0]*sub_position[1])

class Sonar: # Day 1
    def __init__(self, input=1) -> None:
        # self.input_file = r'Data/test.in'
        self.input_file = r'Data/Day1.in' 

        self.df = get_input(self.input_file, input)
    
    def run_day(self, part=0):
        answers = []
        a = [self.individual_depth_measurements(),
            self.sliding_scale_measurements()]
        if part == 0:
            answers.append(a[0])
            answers.append(a[1])
        else:
            answers.append(a[part])

        for i in answers:
            yield i


    def individual_depth_measurements(self, x: list[int] = None) -> int: # Part 1
        if x == None:
            x = self.df

        measurements: int = 0
        list_len: int = len(x)

        for index, num in enumerate(x):
            index = int(index)

            # don't perform the function on the first measurement
            if (index == 0):
                pass
            else:
                if num > x[index-1]:
                    measurements += 1

        # print(f'The answer to part 1 is: {measurements}')
        return measurements

    def sliding_scale_measurements(self, x: list[int] = None) -> int: # Part 2
        if x == None:
            x = self.df

        measurements: int = 0
        last_window: list[int] = None

        for i in range(len(x)-2):
            window = x[i:i+3]
            if last_window == None:
                last_window = window
                pass
            else:
                if sum(window) > sum(last_window):
                    measurements += 1
                last_window = window

        # print(f'The answer to part 2 is: {measurements}')
        return measurements

