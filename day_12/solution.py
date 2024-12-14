from collections import deque, defaultdict
from utils import ints, add_tuples, dirs_2d_4, valid_point_on_2d_grid
import math
from tqdm import trange
f = [x for x in open("input.txt").read().strip().splitlines()]

def flood_fill(i, j):
    s_val = f[i][j]
    q = deque([(i, j)])
    visited = set()
    while q:
        i, j = q.popleft()
        if (i, j) in visited:
            continue
        visited.add((i, j))
        for di, dj in dirs_2d_4:
            ni, nj = i + di, j + dj
            if valid_point_on_2d_grid(ni, nj, f) and f[ni][nj] == s_val:
                q.append((ni, nj))
    return visited

regions = []
seen = set()
for i, line in enumerate(f):
    for j, val in enumerate(line):
        if (i,j) not in seen:
            new_pos = flood_fill(i, j)
            regions.append(new_pos)
            for pos in new_pos:
                seen.add(pos)
p1 = 0
p2 = 0
for region in regions:
    area = len(region)
    perimeter = 0
    num_sides = 0
    for pos in region:
        v = 4
        i,j = pos
        for di, dj in dirs_2d_4:
            ni, nj = i + di, j + dj
            if (ni, nj) in region:
                v -= 1 # if it has a neighbor, it doesn't contribute to the perimeter, so subtract 1 from the count of "open edges"
        perimeter += v # add the number of open edges to the perimeter
    p1 += area * perimeter

    for di, dj in dirs_2d_4:
        side = set() # set of all sides in this direction
        for pos in region: # for each point in the region
            i,j = pos
            ni, nj = i + di, j + dj # go in this direction
            if (ni, nj) not in region: # if it's not in the region, add it to the side
                side.add((ni, nj))
        to_remove = set() # set of sides to remove
        for pos in side:
            i,j = pos
            ni, nj = i + dj, j + di # go perpendicular to the direction
            while (ni, nj) in side: # while it's in the side, add it to the to_remove set // since you're going perpendicular, you'll hit the same side again n-1 times. 
                to_remove.add((ni, nj))
                ni, nj = ni + dj, nj + di
        num_sides += len(side) - len(to_remove)
    p2 += area * num_sides
print(p1)
print(p2)
