from collections import deque, defaultdict
from utils import ints, add_tuples, neighbors_2d, valid_point_on_2d_grid

f = [x for x in open("input.txt").read().strip().split("\n\n")]

walls = set()
boxes = set()
for i, row in enumerate(f[0].splitlines()):
    for j, c in enumerate(row):
        if c == "#":
            walls.add((i, j))
        if c == "@":
            start = (i, j)
        if c == "O":
            boxes.add((i, j))


# print(walls)
# print(boxes)
# print(start)
d_map = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}
curr = start
for action in "".join(f[1].splitlines()):
    di,dj = d_map[action]
    ni, nj = curr[0] + di, curr[1] + dj
    if (ni, nj) in walls:
        continue
    og_ni, og_nj = ni, nj
    if (ni, nj) in boxes:
        # push boxes that are in the way, one step if possible (check if it's a wall)
        while (ni, nj) in boxes:
            ni, nj = ni + di, nj + dj
            if (ni, nj) in walls:
                # we hit a wall, we can't push the box
                break
            if (ni, nj) not in boxes and (ni, nj) not in walls:
                # we can push the box
                boxes.remove((og_ni, og_nj))
                boxes.add((ni, nj))
                curr = (og_ni, og_nj)
                break
        
    else:
        curr = (ni, nj)
    # print(curr) 
p1 =0
for b in boxes:
    p1 += 100 * b[0] + b[1]
print(p1)


f = [x for x in open("input.txt").read().strip().split("\n\n")]

# For part 2, we need to double the width of everything except the robot
def double_width_map(input_map):
    doubled = []
    for line in input_map.splitlines():
        new_line = ""
        for c in line:
            if c == "#":
                new_line += "##"
            elif c == "O":
                new_line += "[]"
            elif c == ".":
                new_line += ".."
            elif c == "@":
                new_line += "@."
        doubled.append(new_line)
    return "\n".join(doubled)

# Parse the doubled map
# walls = set()
# dboxes = set()  # store boxes as (row, left_col, right_col)
doubled_map = double_width_map(f[0])
grid = []
for i, row in enumerate(doubled_map.splitlines()):
    curr_row = []
    for j, c in enumerate(row):
        if c == "#":
            curr_row.append("#")
            walls.add((i, j))
        if c == "@":
            curr_row.append(".")
            start = (i, j)
        if c == "[":  # left side of box
            curr_row.append("[")
            # dboxes.add((i, j, j+1))  # store both coordinates of the box
        if c == "]":  # right side of box
            curr_row.append("]")
            # dboxes.add((i, j-1, j))  # store both coordinates of the box
    grid.append(curr_row)



def solve(G,part2):
    R = len(G)
    C = len(G[0])
    G = [[G[r][c] for c in range(C)] for r in range(R)]
    # print(G)
    if part2:
        BIG_G = []
        for r in range(R):
            row = []
            for c in range(C):
                if G[r][c]=='#':
                    row.append('#')
                    row.append('#')
                if G[r][c]=='O':
                    row.append('[')
                    row.append(']')
                if G[r][c]=='.':
                    row.append('.')
                    row.append('.')
                if G[r][c]=='@':
                    row.append('@')
                    row.append('.')
            BIG_G.append(row)
        G = BIG_G
        C *= 2

    for r in range(R):
        for c in range(C):
            if G[r][c] == '@':
                sr,sc = r,c
                G[r][c] = '.'

    r,c = sr,sc
    for inst in "".join(f[1].splitlines()):
        if inst == '\n':
            continue
        dr,dc = {'^': (-1,0), '>': (0,1), 'v': (1,0), '<': (0,-1)}[inst]
        #print(r,c,inst)
        rr,cc = r+dr,c+dc
        if G[rr][cc]=='#':
            continue
        elif G[rr][cc]=='.':
            r,c = rr,cc
        elif G[rr][cc] in ['[', ']', 'O']:
            Q = deque([(r,c)])
            SEEN = set()
            ok = True
            while Q:
                rr,cc = Q.popleft()
                if (rr,cc) in SEEN:
                    continue
                SEEN.add((rr,cc))
                rrr,ccc = rr+dr, cc+dc
                if G[rrr][ccc]=='#':
                    ok = False
                    break
                if G[rrr][ccc] == 'O':
                    Q.append((rrr,ccc))
                if G[rrr][ccc]=='[':
                    Q.append((rrr,ccc))
                    assert G[rrr][ccc+1]==']'
                    Q.append((rrr,ccc+1))
                if G[rrr][ccc]==']':
                    Q.append((rrr,ccc))
                    assert G[rrr][ccc-1]=='['
                    Q.append((rrr,ccc-1))
            if not ok:
                continue
            while len(SEEN) > 0:
                for rr,cc in sorted(SEEN):
                    rrr,ccc = rr+dr,cc+dc
                    if (rrr,ccc) not in SEEN:
                        assert G[rrr][ccc] == '.'
                        G[rrr][ccc] = G[rr][cc]
                        G[rr][cc] = '.'
                        SEEN.remove((rr,cc))
            r = r+dr
            c = c+dc

    # for r in range(R):
    #    print(''.join(G[r]))
    ans = 0
    for r in range(R):
        for c in range(C):
            if G[r][c] in ['[', 'O']:
                ans += 100*r+c
    return ans

print(solve(f[0].splitlines(), True))

















# curr = start
# for action in "".join(f[1].splitlines()):
#     di,dj = d_map[action]
#     ni, nj = curr[0] + di, curr[1] + dj
#     i,j = curr
#     og_i, og_j = i, j
#     if grid[ni][nj] == "#":
#         continue
#     elif grid[ni][nj] == ".":
#         # push box
#         curr = (ni, nj)
#     elif grid[ni][nj] in "[]":
#         q = deque()
#         q.append((curr))
#         seen = set()
#         ok = True
#         while q:    
#             ci,cj = q.popleft()
#             if (ci,cj) in seen:
#                 continue
#             seen.add((ci,cj))
#             ni,nj = ci + di, cj + dj
#             if grid[ni][nj] == "#":
#                 ok = False
#                 break
#             if grid[ni][nj] =="[":
#                 q.append((ni,nj))
#                 q.append((ni,nj+1))
#             if grid[ni][nj] == "]":
#                 q.append((ni,nj-1))
#         if not ok:
#             continue
#         while len(seen) > 0:
#             for i,j in sorted(seen):
#                 ni, nj = i + di, j + dj
#                 if (ni, nj) not in seen:
#                     assert grid[ni][nj] == "."
#                     grid[ni][nj] = grid[i][j]
#                     grid[i][j] = "."
#                     seen.remove((i,j))
#         curr = (og_i + di, og_j + dj)
# # print(curr)
# p2 = 0
# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         if grid[i][j] == "[":
#             p2 += 100 * i + j
# print(p2)












# Preserving for posterity... it works on the sample but not on the main input. will debug this later.
# def check_box_at(i, j, dboxes):
#     """Check if there's a box at position (i,j) and return which part (left/right)"""
#     for box in dboxes:
#         if box[0] == i and j == box[1]:
#             return True, "left"
#         if box[0] == i and j == box[2]:
#             return True, "right"
#     return False, None

# def can_push_box(i, j, di, dj, dboxes, walls, pushed_boxes=None):
#     print(f"can_push_box {i=} {j=} {di=} {dj=}")
#     """Check if a box at (i,j) can be pushed in direction (di,dj)"""
#     if pushed_boxes is None:
#         pushed_boxes = set()
        
#     has_box, side = check_box_at(i, j, dboxes)
#     if not has_box:
#         return False

#     # Find the full box
#     if side == "right":
#         box = next(box for box in dboxes if box[0] == i and box[2] == j)
#     else:
#         box = next(box for box in dboxes if box[0] == i and box[1] == j)
#     print(f"can_push_box --- current box {box=}")
#     if box in pushed_boxes:  # Prevent infinite recursion
#         return False
#     pushed_boxes.add(box)
    
#     # Check if the destination is clear
#     ni = i + di
#     nj_left = box[1] + dj
#     nj_right = box[2] + dj
#     print(f"can_push_box_before_my_increment {ni=} {nj_left=} {nj_right=}")
#     if di != 0:
#     # Adjust the destination coordinates when pushing from right side leftward
#     # or from left side rightward
#         if side == "right" and dj == -1 or side == "left" and dj == 1:
#             nj_left += dj
#             nj_right += dj
        
#         # Check if destination is blocked by walls
#         if (ni, nj_left) in walls or (ni, nj_right) in walls:
#             return False
#         print(f"can_push_box {ni=} {nj_left=} {nj_right=}")
#         # Check if destination is blocked by other boxes
#         for other_box in dboxes:
#             if other_box[0] == ni and (nj_left in (other_box[1], other_box[2]) or 
#                                     nj_right in (other_box[1], other_box[2])):
#                 # Recursively check if we can push this box
#                 if side == "right":
#                     if not can_push_box(other_box[0], other_box[2], di, dj, dboxes, walls, pushed_boxes):
#                         # print(f"can't push {other_box[0]} {other_box[2]}")
#                         return False
#                 else:
#                     if not can_push_box(other_box[0], other_box[1], di, dj, dboxes, walls, pushed_boxes):
#                         # print(f"can't push {other_box[0]} {other_box[1]}")
#                         return False
#     else:
#         if (ni, nj_left) in walls or (ni, nj_right) in walls:
#             return False
#         # this is going horizontally, so we need to check if there's a box in the way
#         for other_box in dboxes:
#             if dj == -1 and other_box[0] == ni and other_box[2] == nj_left:
#                 if not can_push_box(other_box[0], other_box[2], di, dj, dboxes, walls, pushed_boxes):
#                     return False
#             if dj == 1 and other_box[0] == ni and other_box[1] == nj_right:
#                 if not can_push_box(other_box[0], other_box[1], di, dj, dboxes, walls, pushed_boxes):
#                     return False

#     return True

# def push_boxes(i, j, di, dj, dboxes, pushed_boxes=None):
#     """Push a chain of boxes, returning the new set of boxes"""
#     if pushed_boxes is None:
#         pushed_boxes = set()
    
#     has_box, side = check_box_at(i, j, dboxes)
#     if not has_box:
#         return dboxes
    
#     # Find the box
#     box = next(box for box in dboxes if box[0] == i and (j in (box[1], box[2])))
    
#     if box in pushed_boxes:
#         return dboxes
#     pushed_boxes.add(box)
    
#     # Check the destination
#     ni = i + di
#     nj_left = box[1] + dj
#     nj_right = box[2] + dj
#     if di != 0:
#         # Adjust the destination coordinates when pushing from right side leftward
#         # or from left side rightward
#         if side == "right" and dj == -1 or side == "left" and dj == 1:
#             nj_left += dj
#             nj_right += dj
        
#         # First push any boxes in the way
#         for other_box in list(dboxes):  # Use list to avoid modifying during iteration
#             if other_box[0] == ni and (nj_left in (other_box[1], other_box[2]) or 
#                                     nj_right in (other_box[1], other_box[2])):
#                 if side == "right":
#                     dboxes = push_boxes(other_box[0], other_box[2], di, dj, dboxes, pushed_boxes)
#                 else:
#                     dboxes = push_boxes(other_box[0], other_box[1], di, dj, dboxes, pushed_boxes)
#     else:
#         for other_box in list(dboxes):
#             if dj == -1 and other_box[0] == ni and other_box[2] == nj_left:
#                 dboxes = push_boxes(other_box[0], other_box[2], di, dj, dboxes, pushed_boxes)
#             if dj == 1 and other_box[0] == ni and other_box[1] == nj_right:
#                 dboxes = push_boxes(other_box[0], other_box[1], di, dj, dboxes, pushed_boxes)
    
#     # Now move this box
#     dboxes.remove(box)
#     dboxes.add((box[0] + di, box[1] + dj, box[2] + dj))
    
#     return dboxes
# def print_grid(walls, curr, dboxes):
#     min_i = min(b[0] for b in walls)
#     max_i = max(b[0] for b in walls)
#     min_j = min(b[1] for b in walls)
#     max_j = max(b[1] for b in walls)

#     for i in range(min_i, max_i+1):
#         for j in range(min_j, max_j+1):
#             if (i, j) in walls: 
#                 print("#", end="")
#                 continue    
#             elif (i, j) == curr:
#                 print("@", end="")
#                 continue
#             box_found = False
#             for box in dboxes:
#                 if box[0] == i and j == box[1]:
#                     print("[]", end="")
#                     box_found = True
#                     break
#             for box in dboxes:
#                 if box[0] == i and j == box[2]:
#                     print("", end="")
#                     box_found = True
#                     break
#             if not box_found:
#                 print(".", end="")
#         print()
# # Process moves
# curr = start
# # print_grid(walls, curr, dboxes)
# for action in "".join(f[1].splitlines()):
#     di, dj = d_map[action]
#     ni, nj = curr[0] + di, curr[1] + dj
    
#     if (ni, nj) in walls:
#         continue
        
#     has_box, side = check_box_at(ni, nj, dboxes)
#     if has_box:
#         if can_push_box(ni, nj, di, dj, dboxes, walls):
#             # Push the chain of boxes
#             dboxes = push_boxes(ni, nj, di, dj, dboxes)
#             curr = (ni, nj)
#     else:
#         curr = (ni, nj)
#     print(f"after move {action}")
#     print_grid(walls, curr, dboxes)
#     input("continue?")

# print_grid(walls, curr, dboxes)
# Calculate score
# p2 = 0
# for b in dboxes:
#     p2 += 100 * b[0] + b[1]
# print(p2)
# f = [x for x in open("sample2.txt").read().strip().split("\n\n")]


# walls = set()
# dboxes = set()
# for i, row in enumerate(f[0].splitlines()):
#     for j, c in enumerate(row):
#         if c == "#":
#             walls.add((i, j))
#         if c == "@":
#             start = (i, j)
#         if c == "[":
#             dboxes.add((i, j, j+1))
# print(walls)
# print(dboxes)
# print(start)

# def check_square(i, j, dboxes):
#     for box in dboxes:
#         if box[0] == i and j == box[1]:
#             return True, 1
#         if box[0] == i and j == box[2]:
#             return True, 2
#     return False, 0

# def check_push(i, j, di, dj, dboxes):
#     val, loc = check_square(i, j, dboxes)
#     if val:
#         ni, nj = i + di, j + dj
#         if di != 0:
#             # have to check both left and right of the box above/below
#             if loc == 1:
#                 can_push = check_square(ni, nj, dboxes)[0] and check_square(ni, nj+1, dboxes)[0]
#             else:
#                 can_push = check_square(ni, nj, dboxes)[0] and check_square(ni, nj-1, dboxes)[0]
#         else:
#             can_push = check_square(ni, nj, dboxes)[0]
#         if (ni, nj) in walls:
#             return False
#         if not check_square(ni, nj, dboxes) and (ni, nj) not in walls:
#             return True
#     return False

# for action in "".join(f[1].splitlines()):
#     di,dj = d_map[action]
#     ni, nj = curr[0] + di, curr[1] + dj
#     if (ni, nj) in walls:
#         continue
#     for box in dboxes:
#         if box[0] == ni and nj in box[1:]: # we're pushing a box
#     curr = (ni, nj)
#     print(curr)

# p2 =0
# for b in dboxes:
#     p2 += 100 * b[0] + b[1]
# print(p1)