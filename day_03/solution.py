import re

f = [x.strip() for x in open("input.txt").readlines()]
f = ["".join(f)]
a = 0
for line in f:
    matches = re.findall(r'mul\(\d+,\d+\)', line)
    for mat in matches:
        left = int(mat[4:mat.index(",")])
        right = int(mat[mat.index(",") + 1:][:-1])
        a += (left * right)
print(a)

p2 = 0
for line in f:
    dos = [x.span()[0] for x in re.finditer(r'do\(\)', line)]
    donts = [x.span()[0] for x in re.finditer(r"don't\(\)", line)]
    muls = re.findall(r'mul\(\d+,\d+\)', line)
    mul_indexes = [x.span()[0] for x in re.finditer(r'mul\(\d+,\d+\)', line)]
    assert len(muls) == len(mul_indexes)
    en_map = {}
    for a in mul_indexes:
        max_do = 0
        max_dont = -1
        for d in dos:
            if d < a:
                max_do = max(d, max_do)
        for d in donts:
            if d < a:
                max_dont = max(d, max_dont)
        if max_do > max_dont:
            en_map[a] = True
        else:
            en_map[a] = False
    for mindex, mat in zip(mul_indexes, muls):
        if en_map[mindex]:
            left = int(mat[4:mat.index(",")])
            right = int(mat[mat.index(",") + 1:][:-1])
            p2 += (left * right)
print(p2)