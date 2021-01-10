"""
Day 1: The Tyranny of the Rocket Equation
"""

from utils import get_int_list


def puzzle1():
    masses = get_int_list('day1')
    print(sum(m // 3 - 2 for m in masses))


def fuel_needed(mass):
    needed = mass // 3 - 2
    if needed <= 0:
        return 0
    needed += fuel_needed(needed)
    return needed


def puzzle2():
    masses = get_int_list('day1')
    print(sum(fuel_needed(m) for m in masses))


if __name__ == '__main__':
    puzzle1()
    puzzle2()
