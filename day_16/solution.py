from collections import deque, defaultdict
from utils import dmap
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
            for dir in dmap.keys():
                g.add_node(((i, j), dir))
for n, d in g.nodes:
    di, dj = dmap[d]
    dest = (n[0] + di, n[1] + dj)
    if (dest, d) in g.nodes:
        # connect to destination
        g.add_edge((n, d), (dest, d) , weight=1)
    for nd in dmap.keys():
        if nd == d:
            continue
        # connect to all other directions
        g.add_edge((n, d), (n, nd), weight=1000)

for direction in dmap.keys():
    # connect to end
    g.add_edge((end, direction), "end", weight=0)

print(nx.shortest_path_length(g, (start, "R"), "end", weight="weight"))

paths = nx.all_shortest_paths(g, (start, "R"), "end", weight="weight")

points = set()
for path in paths:
    for node in path:
        points.add(node[0])
print(len(points) - 1)
