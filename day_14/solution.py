from collections import deque, defaultdict
from utils import ints, add_tuples, neighbors_2d, valid_point_on_2d_grid
# import math
# from tqdm import trange
import z3

f = [x for x in open("input.txt").read().strip().splitlines()]
c = defaultdict(list)
num_points = 0
num_uniq_velos = 0
uniq_velos = set()
for i, line in enumerate(f):
    i, j, v_i, v_j = ints(line)
    c[i, j].append((v_i, v_j))
    num_points += 1
    uniq_velos.add((v_i, v_j))
# print(num_points)
# print(len(uniq_velos))
# input("con")
from math import gcd
from functools import reduce

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def lcm_list(numbers):
    return reduce(lcm, numbers)


# grid_i = 11
grid_i = 101
# grid_j = 7
grid_j = 103

cycle = defaultdict(set)
cycle_lens = defaultdict(int)
# seen = set()
iterc = 0
for _ in range(10000):
    iterc += 1
    next_c = defaultdict(list)
    for k, v in c.items():
        for v_i, v_j in v:
            new_loc = (k[0] + v_i) % grid_i, (k[1] + v_j) % grid_j
            if (v_i, v_j) not in cycle_lens and new_loc in cycle[v_i, v_j]:
                cycle_lens[v_i, v_j] = len(cycle[v_i, v_j])
            else:
                cycle[v_i, v_j].add(new_loc)
            next_c[new_loc].append((v_i, v_j))
    c = next_c
    if iterc == 100:
        quadrants = [0] * 4
        for k,v in c.items():
            if k[0] < grid_i // 2 and k[1] < grid_j // 2:
                quadrants[0] += len(v)
            elif k[0] < grid_i // 2 and k[1] > grid_j // 2:
                quadrants[1] += len(v)
            elif k[0] > grid_i // 2 and k[1] < grid_j // 2:
                quadrants[2] += len(v)
            elif k[0] > grid_i // 2 and k[1] > grid_j // 2:
                quadrants[3] += len(v)
        p = 1
        for i in range(4):
            p *= quadrants[i]
        print(p)
    p2_done = False
    for k,v in c.items():
        count = 0
        for di, dj in neighbors_2d:
            ni, nj = k[0] + di, k[1] + dj
            if (ni, nj) in c:
                count += 1
        if count == 8:
            for i in range(grid_i):
                for j in range(grid_j):
                    if (j, i) in c:
                        print("#", end="")
                    else:
                        print(".", end="")
                print()
            print(iterc)
            p2_done = True
            break
    if p2_done:
        break
