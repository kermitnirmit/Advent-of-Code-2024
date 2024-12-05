from collections import deque, Counter, defaultdict
from utils import topological_sort_subset
from heapq import heappush, heappop, heapify

f = open("input.txt").read().strip()
part1, part2 = f.split("\n\n")

before_after = defaultdict(list)
after_before = defaultdict(list)
for line in part1.split("\n"):
    a,b  = [int(x) for x in line.split("|")]
    before_after[a].append(b)
bad_ones = []
c = 0
for line in part2.split("\n"):
    a = [int(x) for x in line.split(",")]
    good = True
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] in before_after[a[j]]:
                good = False
    if good:
        c += a[len(a) // 2]
    else:
        bad_ones.append(a)
print(c)


print(sum(topological_sort_subset(before_after, bad)[len(bad) // 2] for bad in bad_ones))
