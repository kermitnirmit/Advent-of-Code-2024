from collections import deque
from utils import ints

f = [x for x in open("input.txt").read().strip().splitlines()]

def solve(p2 = False):
    sums = []
    for line in f:
        line = line.split(":")
        l = int(line[0])
        r = ints(line[1])
        q = deque([(r[0], 0)])
        while q:
            x, i = q.popleft()
            if x == l and i == len(r) - 1:
                sums.append(l)
                break
            i += 1
            if i < len(r):
                q.append((x + r[i], i))
                q.append((x * r[i], i))
                if p2:
                    q.append((x * 10 ** len(str(r[i])) + r[i], i))
    print(sum(sums))

solve()
solve(True)