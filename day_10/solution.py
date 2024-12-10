from collections import deque, defaultdict
from utils import ints

f = [[int(y) for y in list(x)] for x in open("input.txt").read().strip().splitlines()]

starts = []
for i, line in enumerate(f):
    for j, val in enumerate(line):
        if val == 0:
            starts.append((0, i,j, i, j))

def solve(p2=False):
    q = deque(starts)
    w = defaultdict(int)
    c = 0
    seen = set()
    while q:
        cur = q.popleft()
        v, i,j, si, sj = cur
        if not p2:
            if (i,j, si, sj) in seen:
                continue
            seen.add((i,j, si, sj))
        if v == 9:
            w[(si, sj)] +=1
            c += 1
        else:
            for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < len(f) and 0 <= nj < len(f[0]) and f[ni][nj] == v + 1:
                    q.append((v+1, ni, nj, si, sj))

    print(c)
solve()
solve(p2=True)