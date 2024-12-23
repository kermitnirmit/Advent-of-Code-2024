from collections import deque, defaultdict
from utils import ints
from functools import lru_cache
import networkx as nx
f = [x for x in open("input.txt").read().strip().split("\n")]

g = nx.Graph()

for line in f:
    a, b = line.split("-")
    g.add_edge(a,b)
    g.add_edge(b,a)

qwer = nx.enumerate_all_cliques(g)

c = 0
for a in qwer:
    if len(a) == 3:
        if any(x[0] == 't' for x in a):
            c += 1
print(c)

q = list(nx.find_cliques(g))
q.sort(key=lambda x: len(x), reverse=True)
ans = ",".join(list(sorted(q[0])))
print(len(q[0]), ans)