from collections import deque, defaultdict
from utils import dmap, ints
from heapq import heappush, heappop, heapify
from itertools import combinations
import networkx as nx
import z3
f = [x for x in open("input.txt").read().strip().split("\n\n")]
regs = f[0].split("\n")
registers = []
for i, reg in enumerate(regs):
    registers.append(int(reg.split(":")[1].strip()))
program = ints(f[1].split(":")[1].strip())

def run(nxt_a):
    a = nxt_a
    b = 0
    c =0 
    
    # program = [int(x) for x in program]
    operand_map = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: "a",
        5: "b",
        6: "c",
        7: None
    }

    def get_combo_operand(index):
        val = operand_map[program[index]]
        if type(val) == str:
            if val == "a":
                return a
            elif val == "b":
                return b
            elif val == "c":
                return c
        else:
            return val
    index = 0
    output = []
    while index < len(program):
        inst = program[index]
        if inst == 0:
            numerator = a
            denominator = 2 ** get_combo_operand(index + 1)
            a = numerator // denominator
            index += 2
        elif inst == 1:
            b = b ^ program[index + 1]
            index += 2
        elif inst == 2:
            b = get_combo_operand(index + 1) % 8
            index += 2
        elif inst == 3:
            if a == 0:
                index += 2
            else:
                index = program[index + 1]
        elif inst == 4:
            b = b ^ c
            index += 2
        elif inst == 5:
            output.append(get_combo_operand(index + 1) % 8)
            index += 2
        elif inst == 6:
            numerator = a
            denominator = 2 ** get_combo_operand(index + 1)
            b = numerator // denominator
            index += 2
        elif inst == 7:
            numerator = a
            denominator = 2 ** get_combo_operand(index + 1)
            c = numerator // denominator
            index += 2
        else:
            break

    # print(output)
    return ",".join(map(str, output))

print(run(registers[0]))
o = z3.Optimize()
s = z3.BitVec("s", 64)
a, b, c = s, 0, 0
for x in program:
    # 2,4 -> B = A mod 8
    # 1,5 -> B = B ^ 5
    # 7,5 -> C = A / 2^B
    # 1,6 -> B = B ^ 6
    # 4,2 -> B = B ^ C
    # 5,5 -> output B mod 8
    # 0,3 -> A = A / 8
    # 3,0 -> restart

    b = a % 8
    b = b ^ 5
    c = a >> b
    b = b ^ 6
    b = b ^ c
    a = a >> 3
    o.add(b % 8 == x)
o.add(a == 0)
o.minimize(s)
assert str(o.check()) == "sat"
m = o.model()
print(m[s].as_long())


