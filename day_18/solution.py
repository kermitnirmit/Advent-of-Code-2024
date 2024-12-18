from collections import deque
from utils import ints, dirs_2d_4
from heapq import heappush, heappop, heapify
from itertools import combinations
from collections import Counter
import z3
f = [x for x in open("input.txt").read().strip().split("\n")]


def is_reachable(i, target):
    points = set()
    start = (0,0)
    q = deque([start])
    for line in f[:i]:
        x,y = ints(line)
        points.add((x,y))

    target = (70, 70)
    seen = set()
    q = deque([(start, 0)])
    p1 = 0
    while q:
        pos, dist = q.popleft()
        if pos == target:
            p1 = dist
            break
            
        x, y = pos
        for dx, dy in dirs_2d_4:
            nx = x + dx
            ny = y + dy
            npos = (nx, ny)
            if npos not in seen and npos not in points and 0 <= nx <= 70 and 0 <= ny <= 70:
                seen.add(npos)
                q.append((npos, dist + 1))
    if p1 > 0:
        return True, p1
    return False, 0

print(is_reachable(1024, (70, 70))[1])
l = 1024
r = len(f) 
while l < r-1:
    m = (l + r) // 2
    if is_reachable(m, (70, 70))[0]:
        l = m
    else:
        r = m - 1

print(f[l])

