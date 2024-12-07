from collections import deque, Counter, defaultdict
from utils import topological_sort_subset, dirs_2d_4, add_tuples
from heapq import heappush, heappop, heapify

f = [list(x) for x in open("input.txt").read().strip().splitlines()]

v = set()
super_v = set()
start = None
possible_blocking_points = set()
for i in range(len(f)):
    for j in range(len(f[i])):
        if f[i][j] == "^":
            start = (i,j)
        if f[i][j] == ".":
            possible_blocking_points.add((i,j))
# print(start)
q = deque([(start, (-1, 0), 0)])
# v.add((start, (-1,0)))
points = set(start)
def valid_point(i, j):
    return 0 <= i < len(f) and 0 <= j < len(f[i])


while q:
    c, d, step = q.popleft()
    if (c,d) in v:
        continue
    else:
        v.add((c, d))
        super_v.add((c,d, step))
        points.add(c)
        ci, cj = c
        di, dj = d
        ni, nj = ci + di, cj + dj
        if valid_point(ni, nj) and f[ni][nj] == "#":
            # turn right
            i = dirs_2d_4.index(d)
            nd = dirs_2d_4[(i + 1) % 4]
            real_ni = ci + nd[0]
            real_nj = cj + nd[1]
            if valid_point(real_ni, real_nj):
                q.append(((real_ni, real_nj), nd, step + 1))
        elif valid_point(ni, nj) and f[ni][nj] != "#":
            # keep going same direction
            q.append(((ni, nj), d, step + 1))
        elif not valid_point(ni, nj):
            # out of the map?
            break
c = 0
for i in range(len(f)):
    for j in range(len(f[i])):
        if (i,j) in points:
            c += 1
print(c)
def is_open(i, j, g):
    return g[i][j] != "#"
# v is all the places we've been, so if we can add an obstacle that would force us to hit a
def traverse(g, ol):
    q = deque([(start, (-1, 0))])
    oli, olj = ol
    g[oli][olj] = "#"
    s = 0
    seen = set()
    while q:
        c, d = q.popleft()
        if c in seen:
            s += 1
        else:
            s = 0
        if s > 1000:
            g[oli][olj] = "."
            return True
        seen.add(c)
        ni, nj = add_tuples(c,d)
        if not valid_point(ni, nj):
            break
        if is_open(ni, nj, g):
            q.append(((ni, nj), d))
        else:
            while not is_open(ni, nj, g):
                i = dirs_2d_4.index(d)
                d = dirs_2d_4[(i + 1) % 4]
                ni, nj = add_tuples(c, d)
            q.append(((ni, nj), d))
    g[oli][olj] = "."
    return False

p2 = 0
for p in possible_blocking_points:
    p2 += traverse(f, p)
print(p2)
