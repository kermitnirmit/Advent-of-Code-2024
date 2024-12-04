from collections import deque, Counter

f = [x.strip() for x in open("input.txt").readlines()]
neighbors_2d = [(x, y) for y in range(-1, 2) for x in range(-1, 2) if (x, y) != (0, 0)]
diag_neighbors = [(1, 1), (1, -1), (-1, -1), (-1, 1)]


def valid_point(i, j):
    return 0 <= i < len(f) and 0 <= j < len(f[i])


a = 0
starts = []
for i in range(len(f)):
    for j in range(len(f[i])):
        if f[i][j] == "X":
            starts.append((i, j, (0, 0), 0))
target = "XMAS"
q = deque(starts)

while q:
    ci, cj, d, i = q.popleft()
    if i == 3 and f[ci][cj] == "S":
        a += 1
    else:
        if d == (0, 0):
            for di, dj in neighbors_2d:
                ni, nj = ci + di, cj + dj
                if valid_point(ni, nj) and f[ni][nj] == "M":
                    q.append((ni, nj, (di, dj), 1))
        else:
            di, dj = d
            ni, nj = ci + di, cj + dj
            if valid_point(ni, nj) and f[ni][nj] == target[i + 1]:
                q.append((ni, nj, (di, dj), i + 1))
print(a)

p2 = 0

starts = []
for i in range(len(f)):
    for j in range(len(f[i])):
        if f[i][j] == "A":
            starts.append((i, j))

q = deque(starts)

while q:
    ci, cj = q.popleft()
    n_vals = []
    for di, dj in diag_neighbors:
        ni, nj = ci + di, cj + dj
        if valid_point(ni, nj):
            n_vals.append(f[ni][nj])
    valid = False
    if "X" in n_vals:
        continue
    if len(n_vals) == 4:
        c = Counter(n_vals)
        if c["M"] != 2 or c["S"] != 2:
            continue
        for i in range(len(n_vals)):
            valid = n_vals[i] != n_vals[i - 2]
    p2 += valid
print(p2)
