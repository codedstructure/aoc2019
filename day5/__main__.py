"""
Day 5: Sunny with a Chance of Asteroids
"""

from utils import get_int_list
from intcode.cpu import IntcodeCpu


def puzzle1():
    prog = get_int_list('day5')
    cpu = IntcodeCpu(prog)
    cpu.input_queue.put(1)
    cpu.run()
    print(cpu.output_queue.get())


def puzzle2():
    prog = get_int_list('day5')
    cpu = IntcodeCpu(prog)
    cpu.input_queue.put(5)
    cpu.run()
    print(cpu.output_queue.get())


if __name__ == '__main__':
    puzzle1()
    puzzle2()
