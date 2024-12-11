from collections import deque, defaultdict
from utils import ints
import math
from tqdm import trange
f = ints(open("input.txt").read().strip().splitlines()[0])


def solve(p2=False):
    c = defaultdict(int)
    for i in f:
        c[i] += 1
    for _ in trange(75 if p2 else 25):
        n_c = defaultdict(int)
        for k,v in c.items():
            if k == 0:
                n_c[1] += v
            elif len(str(k)) % 2 == 0:
                left = str(k)[:len(str(k))//2]
                right = str(k)[len(str(k))//2:]
                n_c[int(left)] += v
                n_c[int(right)] += v
            else:
                n_c[k*2024] += v

        c = n_c
    return sum(c.values())

print(solve())
print(solve(p2=True))

