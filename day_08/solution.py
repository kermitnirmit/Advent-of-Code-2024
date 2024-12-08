from collections import defaultdict
from utils import ints, valid_point_on_2d_grid
from itertools import combinations

f = [x for x in open("input.txt").read().strip().splitlines()]

nodes = defaultdict(list)
for i, line in enumerate(f):
    for j, c in enumerate(line):
        if c != ".":
            nodes[c].append((i, j))

anti_nodes = set()
for node in nodes:
    for a, b in combinations(nodes[node], 2):
        di, dj = a[0] - b[0], a[1] - b[1]
        if valid_point_on_2d_grid(a[0] + di, a[1] + dj, f):
            anti_nodes.add((a[0] + di, a[1] + dj))
        if valid_point_on_2d_grid(b[0] - di, b[1] - dj, f):
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
        while valid_point_on_2d_grid(ci + di, cj + dj, f):
            anti_nodes.add((ci + di, cj + dj))
            ci += di
            cj += dj
        ci, cj = b
        while valid_point_on_2d_grid(ci - di, cj - dj, f):
            anti_nodes.add((ci - di, cj - dj))
            ci -= di
            cj -= dj
print(len(anti_nodes))