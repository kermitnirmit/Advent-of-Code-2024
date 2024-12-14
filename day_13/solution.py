from collections import deque, defaultdict
from utils import ints, add_tuples, dirs_2d_4, valid_point_on_2d_grid
# import math
# from tqdm import trange
import z3

f = [x for x in open("input.txt").read().strip().split("\n\n")]
prizes_and_buttons = {}
a_cost = 3
b_cost = 1
for line in f:
    a = None
    b = None
    target = None
    for i, l in enumerate(line.split("\n")):
        if i == 2:
            q,w = ints(l)
            prizes_and_buttons[(q,w)] = (a,b)
        if i == 0:
            a = ints(l)
        if i == 1:
            b = ints(l)
# c = 0
# print(z3)
def solve_aoc(p2=False):
    c = 0
    for k,v in prizes_and_buttons.items():
        solver = z3.Solver()
        # find linear combination of a and b that equals k
        x = z3.Int("x")
        y = z3.Int("y")
        solver.add((x * v[0][0]) + (y * v[1][0]) == k[0] + (10000000000000 if p2 else 0))
        solver.add((x * v[0][1]) + (y * v[1][1]) == k[1] + (10000000000000 if p2 else 0))
        solver.add(x >= 0)
        solver.add(y >= 0)

        if solver.check() == z3.sat:  # Note: sat instead of z3.sat
            m = solver.model()
            c += (a_cost * m[x].as_long() + b_cost * m[y].as_long())
    print(c)

solve_aoc()
solve_aoc(p2=True)
