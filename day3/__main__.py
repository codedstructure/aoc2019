"""
Day 3: Crossed Wires
"""

from utils import get_lines


class WireTrace:
    def __init__(self, instructions, check_trace=None):
        self.trace = set()
        self.trace_delay = {}
        self.check_trace = check_trace
        self.pos_x = 0
        self.pos_y = 0
        self.delay = 0
        self.min_distance = 1e12   # +inf...
        self.min_delay = 1e12      # +inf...
        for inst in instructions:
            self.move(inst)

    def move(self, inst):
        direction, count = inst[0], int(inst[1:])
        dx = 0
        dy = 0
        if direction == 'U':
            dx, dy = 0, -1
        elif direction == 'D':
            dx, dy = 0, 1
        elif direction == 'L':
            dx, dy = -1, 0
        elif direction == 'R':
            dx, dy = 1, 0
        for _ in range(count):
            self.delay += 1
            self.pos_x += dx
            self.pos_y += dy
            self.trace.add((self.pos_x, self.pos_y))
            self.trace_delay[(self.pos_x, self.pos_y)] = self.delay
            self.check_collision()

    def check_collision(self):
        if not self.check_trace:
            return
        if (self.pos_x, self.pos_y) in self.check_trace.trace:
            self.update_distance()
            self.update_delay()

    def update_distance(self):
        distance = abs(self.pos_x) + abs(self.pos_y)
        if distance < self.min_distance:
            self.min_distance = distance

    def update_delay(self):
        delay = self.delay + self.check_trace.trace_delay[(self.pos_x, self.pos_y)]
        if delay < self.min_delay:
            self.min_delay = delay


def puzzle1():
    wire1, wire2 = get_lines('day3')
    wire1 = wire1.split(',')
    wire2 = wire2.split(',')
    trace1 = WireTrace(wire1)
    trace2 = WireTrace(wire2, trace1)

    print(trace2.min_distance)


def puzzle2():
    wire1, wire2 = get_lines('day3')
    wire1 = wire1.split(',')
    wire2 = wire2.split(',')
    trace1 = WireTrace(wire1)
    trace2 = WireTrace(wire2, trace1)

    print(trace2.min_delay)


if __name__ == '__main__':
    puzzle1()
    puzzle2()
