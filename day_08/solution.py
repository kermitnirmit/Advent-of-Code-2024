from collections import defaultdict
from utils import ints
from itertools import combinations

f = [x for x in open("input.txt").read().strip().splitlines()]

def valid_point(i, j):
    return 0 <= i < len(f) and 0 <= j < len(f[0])

nodes = defaultdict(list)
for i, line in enumerate(f):
    for j, c in enumerate(line):
        if c != ".":
            nodes[c].append((i, j))

anti_nodes = set()
for node in nodes:
    for a, b in combinations(nodes[node], 2):
        di, dj = a[0] - b[0], a[1] - b[1]
        if valid_point(a[0] + di, a[1] + dj):
            anti_nodes.add((a[0] + di, a[1] + dj))
        if valid_point(b[0] - di, b[1] - dj):
            anti_nodes.add((b[0] - di, b[1] - dj))
print(len(anti_nodes))


# part 2
anti_nodes = set()
for node in nodes:
    for a, b in combinations(nodes[node], 2):
        di, dj = a[0] - b[0], a[1] - b[1]
        anti_nodes.add(a)
        anti_nodes.add(b)
        ci, cj = a
        while valid_point(ci + di, cj + dj):
            anti_nodes.add((ci + di, cj + dj))
            ci += di
            cj += dj
        ci, cj = b
        while valid_point(ci - di, cj - dj):
            anti_nodes.add((ci - di, cj - dj))
            ci -= di
            cj -= dj
print(len(anti_nodes))