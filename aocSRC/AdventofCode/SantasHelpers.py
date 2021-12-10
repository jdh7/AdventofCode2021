import sys, os
from typing import Any

def get_input(input_file, x=1) -> list[Any]:
    if x == 1:
        with open(input_file, 'r') as f:
            df: list[Any] = [int(line.strip()) for line in f] #[int(line.strip()) for line in f]
        return df
    if x == 2:
        with open(input_file, 'r') as f:
            df = [line.split() for line in f]
        return df
    if x == 3:
        with open(input_file, 'r') as f:
            df: list[Any] = [line.strip() for line in f] #[int(line.strip()) for line in f]
        return df

def bin_to_dec(x:list[str])->int:
    return int((''.join(x)), 2)

def most_common_digit(df:list[str], choice=True) -> list[str]:
    digit_lists: list[lists[str]] = [[] for _ in range(len(df[0]))]
    most_common_digit: list[str] = [[] for _ in range(len(df[0]))]
    least_common_digit: list[str] = [[] for _ in range(len(df[0]))]

    for item in range(len(df)):
        for c in range(len(df[0])):
            digit_lists[c].append(df[item][c])
    
    for i in range(len(digit_lists)):
        most_common_digit[i] = max(digit_lists[i], key =
            digit_lists[i].count)

        least_common_digit[i] = min(digit_lists[i], key =
            digit_lists[i].count)

        if most_common_digit[i] == least_common_digit[i]:
            most_common_digit[i] = '1'

        if most_common_digit[i] == least_common_digit[i]:
            least_common_digit[i] = '0'

    _x = [least_common_digit, most_common_digit]
    return _x[choice] 


