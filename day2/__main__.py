"""
Day 2: 1202 Program Alarm
"""

from itertools import product
from utils import get_int_list
from intcode.cpu import IntcodeCpu


def puzzle1():
    prog = get_int_list('day2')
    prog[1] = 12
    prog[2] = 2
    cpu = IntcodeCpu(prog)
    cpu.run()
    print(cpu[0])


def puzzle2():
    prog = get_int_list('day2')
    cpu = IntcodeCpu(prog)
    for noun, verb in product(range(100), range(100)):
        cpu.push_state()
        cpu[1] = noun
        cpu[2] = verb
        try:
            cpu.run()
        except (IndexError, ValueError):
            continue
        if cpu[0] == 19690720:
            break
        cpu.pop_state()
    else:
        print("Not Found")
        return
    print(100 * noun + verb)


if __name__ == '__main__':
    puzzle1()
    puzzle2()
