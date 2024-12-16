from collections import deque, defaultdict
from utils import ints, add_tuples, neighbors_2d, valid_point_on_2d_grid, dirs_2d_4
from heapq import heappush, heappop, heapify
from itertools import combinations
import networkx as nx
f = [x for x in open("input.txt").read().strip().splitlines()]
# The Reindeer start on the Start Tile (marked S) facing East and need to reach the End Tile (marked E). They can move forward one tile at a time 
# (increasing their score by 1 point), but never into a wall (#). They can also rotate clockwise or counterclockwise
#  90 degrees at a time (increasing their score by 1000 points).


for i, line in enumerate(f):
    for j, c in enumerate(line):
        if c == "S":
            start = (i, j)
        elif c == "E":
            end = (i, j)
print(start, end)


g = nx.DiGraph()
for i in range(len(f)):
    for j in range(len(f[0])):
        if f[i][j] != "#":
            for dir in "NESW":
                g.add_node(((i, j), dir))
for n, d in g.nodes:
    if d == "N":
        dest = (n[0] - 1, n[1])
    elif d == "S":
        dest = (n[0] + 1, n[1])
    elif d == "E":
        dest = (n[0], n[1] + 1)
    elif d == "W":
        dest = (n[0], n[1] - 1)
    if (dest, d) in g.nodes:
        # connect to destination
        g.add_edge((n, d), (dest, d) , weight=1)
    for nd in "NESW":
        if nd == d:
            continue
        # connect to all other directions
        g.add_edge((n, d), (n, nd), weight=1000)

for direction in "NESW":
    # connect to end
    g.add_edge((end, direction), "end", weight=0)

print(nx.shortest_path_length(g, (start, "E"), "end", weight="weight"))

paths = nx.all_shortest_paths(g, (start, "E"), "end", weight="weight")

points = set()
for path in paths:
    for node in path:
        points.add(node[0])
print(len(points) - 1)
