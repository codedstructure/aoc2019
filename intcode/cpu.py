"""
Intcode CPU interpreter
"""

from queue import Queue


class IntcodeCpu:
    def __init__(self, program):
        self.ip = 0
        self.memory = program
        self.save_stack = []
        self.input_queue = Queue()
        self.output_queue = Queue()

    p_count = {
        1: 3, 2: 3, 7: 3, 8: 3,
        5: 2, 6: 2,
        3: 1, 4: 1,
        99: 0
    }

    def run(self):
        while True:
            opcode, params = self.fetch()
            if opcode == 99:
                break
            prev_ip = self.ip
            self.execute(opcode, params)
            if self.ip == prev_ip:
                self.ip += (1 + len(params))

    def fetch(self):
        opcode = self.memory[self.ip]
        parameter_mode, opcode = divmod(opcode, 100)

        # 123 -> [3, 2, 1]; 45 -> [5, 4, 0] etc.
        pmode = [int(x) for x in reversed(f'{parameter_mode:03d}')]

        params = []
        for idx in range(self.p_count[opcode]):
            params.append(self.memory[self.ip + idx + 1])
        return opcode, tuple(zip(pmode, params))

    def execute(self, op, params):
        # print(self.ip, op, params)
        if op == 1:  # add
            src1, src2, dest = params
            self.store(dest, self.load(src1) + self.load(src2))
        elif op == 2:  # multiply
            src1, src2, dest = params
            self.store(dest, self.load(src1) * self.load(src2))
        elif op == 3:  # input
            dest = params[0]
            value = self.get_input()
            self.store(dest, value)
        elif op == 4:  # output
            dest = params[0]
            value = self.load(dest)
            self.output(value)
        elif op == 5:  # jump-if-true
            src, jmp = params
            value = self.load(src)
            if value != 0:
                self.ip = self.load(jmp)
        elif op == 6:  # jump-if-false
            src, jmp = params
            value = self.load(src)
            if value == 0:
                self.ip = self.load(jmp)
        elif op == 7:  # less-than
            src1, src2, dest = params
            if self.load(src1) < self.load(src2):
                self.store(dest, 1)
            else:
                self.store(dest, 0)
        elif op == 8:  # equals
            src1, src2, dest = params
            if self.load(src1) == self.load(src2):
                self.store(dest, 1)
            else:
                self.store(dest, 0)
        elif op == 99:
            pass
        else:
            raise ValueError(f'unhandled opcode {op}')

    def load(self, param):
        pmode, param = param
        if pmode == 1:
            return param
        elif pmode == 0:
            return self[param]
        else:
            raise ValueError(f"Invalid parameter mode {pmode}")

    def store(self, param, value):
        pmode, param = param
        if pmode == 1:
            raise ValueError("Cannot store to immediate parameter")
        elif pmode == 0:
            self[param] = value
        else:
            raise ValueError(f"Invalid parameter mode {pmode}")

    def __str__(self):
        return ','.join(str(m) for m in self.memory)

    def __getitem__(self, idx):
        return self.memory[idx]

    def __setitem__(self, idx, val):
        try:
            self.memory[idx] = val
        except IndexError:
            print(f"Bus error writing {val} to {idx}")
            raise

    def push_state(self):
        self.save_stack.append((self.ip, self.memory.copy()))

    def pop_state(self):
        self.ip, self.memory = self.save_stack.pop()

    def get_input(self):
        return self.input_queue.get()

    def output(self, value):
        print(value)
        self.output_queue.put(value)
