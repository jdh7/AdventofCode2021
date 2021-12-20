from ElfTech import *
from SquidBingo import SquidBingo
from VentNav import VentNav
from LanternFish import Fish_counter
from whalewhalewhale import Crab_scooter
from SignalWires import Wire_decoder

# current_day = input("Please input the current day number: ")
# current_part = input("Please input the current part (0 for both pars): ")
current_day = 8
current_part = 0

day_apps = [Sonar(),
           Sub_driving(),
           LifeSupport(), 
           SquidBingo(),
           VentNav(),
           Fish_counter(),
           Crab_scooter(),
           Wire_decoder()]


if __name__ == '__main__':
    a = [i for i in day_apps[current_day-1].run_day(current_part)]
    print(f'For day {current_day}:')
    for i,e in enumerate(a):
        print(f'The answer to part {i+1} is: {e}')
