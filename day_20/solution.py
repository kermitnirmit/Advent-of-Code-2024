from collections import deque, defaultdict

f = [x for x in open("input.txt").read().strip().split("\n")]

for i, line in enumerate(f):
    for j, c in enumerate(line):
        if c == "S":
            start = (i, j)
        elif c == "E":
            end = (i, j)

points_to_remaining = {}
seen = set()
q = [(start, 0, [start])]
q = deque(q)
final_path = []
while q:
    curr, dist, path = q.popleft()
    if curr == end:
        # print(dist)
        final_path = path
        break
    if curr in seen:
        continue
    seen.add(curr)
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ni, nj = curr[0] + di, curr[1] + dj
        if 0 <= ni < len(f) and 0 <= nj < len(f[0]) and f[ni][nj] != "#":
            q.append(((ni, nj), dist + 1, path + [(ni, nj)]))
no_shortcut_distance = dist
for i, point in enumerate(final_path):
    points_to_remaining[point] = len(final_path) - i - 1

def solve(max_cheat_dist, threshold_to_count=100):
    possibles = []

    for i, curr in enumerate(final_path):
        for di in range(-max_cheat_dist, max_cheat_dist + 1):
            for dj in range(-max_cheat_dist, max_cheat_dist + 1):
                if abs(di) + abs(dj) <= max_cheat_dist:  # Manhattan distance of max_cheat_dist
                    ni, nj = curr[0] + di, curr[1] + dj 
                    if 0 <= ni < len(f) and 0 <= nj < len(f[0]) and f[ni][nj] != "#":
                        possibles.append((i + abs(di) + abs(dj) + points_to_remaining[(ni, nj)], (curr, (ni, nj))))

    c = defaultdict(set)
    for possible in possibles:
        n_dist, shortcut_used = possible
        c[no_shortcut_distance - n_dist].add(shortcut_used)

    p1 = 0
    for k,v in c.items():
        if k >= threshold_to_count:
            p1 += len(v)
    return p1

print(solve(2))
print(solve(20))