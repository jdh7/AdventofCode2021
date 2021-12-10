# from ElfTech import *
# from SantasHelpers import *
from ElfTech import *

data = r'Data/test.in'

# current_day = input("Please input the current day number: ")
# current_part = input("Please input the current part (0 for both pars): ")
current_day = 1
current_part = 0

day_apps = [Sonar(),
           Sub_driving(),
           LifeSupport()]




if __name__ == '__main__':
    a = [i for i in day_apps[current_day-1].run_day(current_part)]
    for i,e in enumerate(a):
        print(f'The answer to part {i+1} is: {e}')
