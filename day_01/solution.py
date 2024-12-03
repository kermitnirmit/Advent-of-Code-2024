from collections import Counter
f = [x.strip() for x in open("input.txt").readlines()]

lefts = []
rights = []
for line in f:
    vals = line.split(" ")
    lefts.append(int(vals[0]))
    rights.append(int(vals[-1]))

lefts.sort()
rights.sort()

c = 0
for a, b in zip(lefts,rights):
    c += abs(a-b)
print(c)
C = Counter(rights)
p = 0
for a in lefts:
    p += a * C[a]
print(p)
