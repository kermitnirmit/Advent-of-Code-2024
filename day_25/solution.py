from collections import deque, defaultdict
from utils import ints
from functools import lru_cache
import networkx as nx
import parse as p
import graphviz
f = [x for x in open("input.txt").read().strip().split("\n\n")]
locks = []
keys = []
for p in f:
    lines = p.splitlines()
    # print(lines)
    if lines[0] == "#####":
        ret = [0] * len(lines[1])
        for line in lines[1:]:
            # print(line)
            for j in range(len(line)):
                if line[j] == "#":
                    ret[j] += 1
        locks.append(ret)
    elif lines[-1] == "#####":
        ret = [0] * len(lines[0])
        for line in lines[:-1]:
            for j in range(len(line)):
                if line[j] == "#":
                    ret[j] += 1
        keys.append(ret)
# print(keys)
# print(locks)
c = 0
for k in keys:
    for l in locks:
        good = True
        for q,w in zip(k,l):
            if q + w > 5:
                good = False
                break
        c += good
print(c)