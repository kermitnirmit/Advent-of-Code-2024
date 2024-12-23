from collections import deque, defaultdict
from utils import ints
from functools import lru_cache, cache
from tqdm import trange
import networkx as nx
f = [x for x in open("input.txt").read().strip().split("\n")]

num_pad = {'7': (0,0), '8': (0,1), '9': (0,2), '4': (1,0), '5': (1,1), '6': (1,2), '1': (2,0), '2': (2,1), '3': (2,2), '0': (3,1), 'A': (3,2)}
dir_pad = {'^': (0,1), 'A': (0,2), '<': (1,0), 'v': (1,1), '>': (1,2)}

buttons = {
    "7": ((0, 0), ">v"), "8": ((0, 1), "<>v"), "9": ((0, 2), "<v"),
    "4": ((1, 0), ">^v"), "5": ((1, 1), "<>^v"), "6": ((1, 2), "<^v"),
    "1": ((2, 0), "^>"), "2": ((2, 1), "<>^v"), "3": ((2, 2), "<^v"),
    "0": ((3, 1), ">^"), 'A': ((3, 2), "<^")
}

buttons2 = {
    'A': {"A": [""], "^": ["<"], ">": ["v"], "v": ["<v", "v<"], "<": ["v<<"]},
    '^': {"^": [""], "A": [">"], "v": ["v"], "<": ["v<"], ">": ["v>"]},
    'v': {"v": [""], "A": ["^>", ">^"], "^": ["^"], "<": ["<"], ">": [">"]},
    '<': {"<": [""], "A": [">>^"], "^": [">^"], "v": [">"], ">": [">>"]},
    '>': {">": [""], "A": ["^"], "^": ["^<", "<^"], "v": ["<"], "<": ["<<"]},
}


# num_pad_best_path = {((0,0), (0,1)): '>',)}

@lru_cache(None)
def generate_num_seq(num_seq):
    start = num_pad['A']
    seq = []
    for val in num_seq:
        updo = []
        di = num_pad[val][0] - start[0]
        dj = num_pad[val][1] - start[1]
        for _ in range(abs(di)):
            if di > 0:
                updo.append('v')
            else:
                updo.append('^')
        leri = []
        for _ in range(abs(dj)):
            if dj > 0:
                leri.append('>')
            else:
                leri.append('<')

        if start[0] == 3 and num_pad[val][1] == 0:
            # bottom row going to the left column
            seq.extend(updo)
            seq.extend(leri)
        elif start[1] == 0 and num_pad[val][0] == 3:
            # left column going to the bottom row
            seq.extend(leri)
            seq.extend(updo)
        else:
            if dj < 0:
                # left
                seq.extend(leri)
                seq.extend(updo)
            elif dj > 0:    
                # right
                seq.extend(updo)
                seq.extend(leri)
            else:
                # not up or down
                seq.extend(updo)
        seq.append('A')
        start = num_pad[val]
    return "".join(seq)


@lru_cache(None)
def generate_vals_from_start_to_dest(s, d):
    seq = []
    start = dir_pad[s]
    dest = dir_pad[d]
    updo = []
    di = dest[0] - start[0]
    dj = dest[1] - start[1]
    for _ in range(abs(di)):
        if di > 0:
            updo.append('v')
        else:
            updo.append('^')
    leri = []
    for _ in range(abs(dj)):
        if dj > 0:
            leri.append('>')
        else:
            leri.append('<')
    if start[1] == 0:
        # bottom starting on the <
        seq.extend(leri)
        seq.extend(updo) 
    elif dest[1] == 0:
        # going to the left column
        seq.extend(updo)
        seq.extend(leri)
    else:
        if dj < 0:
            # left
            seq.extend(leri)
            seq.extend(updo)
        elif dj > 0:    
            # right
            seq.extend(updo)
            seq.extend(leri)
        else:
            # not left or right, only updown
            seq.extend(updo)
    seq.append('A')
    return "".join(seq)



@lru_cache(None)
def generate_dir_seq(dir_seq):
    start = dir_pad['A']
    seq = []
    for val in dir_seq:
        updo = []
        di = dir_pad[val][0] - start[0]
        dj = dir_pad[val][1] - start[1]
        for _ in range(abs(di)):
            if di > 0:
                updo.append('v')
            else:
                updo.append('^')
        leri = []
        for _ in range(abs(dj)):
            if dj > 0:
                leri.append('>')
            else:
                leri.append('<')

        if start[1] == 0:
            # bottom starting on the <
            seq.extend(leri)
            seq.extend(updo) 
        elif dir_pad[val][1] == 0:
            # going to the left column
            seq.extend(updo)
            seq.extend(leri)
        else:
            if dj < 0:
                # left
                seq.extend(leri)
                seq.extend(updo)
            elif dj > 0:    
                # right
                seq.extend(updo)
                seq.extend(leri)
            else:
                # not left or right, only updown
                seq.extend(updo)
        seq.append('A')
        start = dir_pad[val]
    return "".join(seq)


# p1 = 0
# for line in f:
#     left = ints(line)
#     m = generate_dir_seq(generate_dir_seq(generate_num_seq(line)))
#     print(line, m, len(m))
#     p1 += len(m) * left[0]
#     # p1 += len(generate_dir_seq(generate_dir_seq(generate_num_seq(line)))) * left[0]
#     # print("line", line, "left", left)
p1 = 0
for line in f:
    left = ints(line)
    curr = generate_num_seq(line)
    for i in range(2):
        curr = generate_dir_seq(curr)
    p1 += len(curr) * left[0]
print(p1)


# p1 = 0
# for line in f:
#     left = ints(line)
#     curr = generate_num_seq(line)
#     for i in trange(20):
#         q = ""
#         s = "A"
#         print(len(curr))
#         for letter in curr:
#             d = letter
#             q += generate_vals_from_start_to_dest(s, d)
#             s = d
#         curr = q
#     p1 += len(curr) * left[0]
# print(p1)


# https://github.com/marcodelmastro/AdventOfCode2024/blob/main/Day21.ipynb
num_pad = nx.DiGraph()
num_pad.add_edges_from([("A", "0"), ("A", "3")])
num_pad.add_edges_from([("0", "2"), ("0", "A")])
num_pad.add_edges_from([("1", "4"), ("1", "2")])
num_pad.add_edges_from([("2", "1"), ("2", "5"), ("2", "3"), ("2", "0")])
num_pad.add_edges_from([("3", "2"), ("3", "6"), ("3", "A")])
num_pad.add_edges_from([("4", "7"), ("4", "5"), ("4", "1")])
num_pad.add_edges_from([("5", "4"), ("5", "8"), ("5", "6"), ("5", "2")])
num_pad.add_edges_from([("6", "5"), ("6", "9"), ("6", "3")])
num_pad.add_edges_from([("7", "8"), ("7", "4")])
num_pad.add_edges_from([("8", "7"), ("8", "5"), ("8", "9")])
num_pad.add_edges_from([("9", "8"), ("9", "6")])

num_pad_move = {
    ('A', '0'): '<', ('A', '3'): '^',
    ('0', '2'): '^', ('0', 'A'): '>',
    ('1', '4'): '^', ('1', '2'): '>', 
    ('2', '1'): '<', ('2', '5'): '^', ('2', '3'): '>', ('2', '0'): 'v',
    ('3', '2'): '<', ('3', '6'): '^', ('3', 'A'): 'v', 
    ('4', '7'): '^', ('4', '5'): '>', ('4', '1'): 'v', 
    ('5', '4'): '<', ('5', '8'): '^', ('5', '6'): '>', ('5', '2'): 'v', 
    ('6', '5'): '<', ('6', '9'): '^', ('6', '3'): 'v',
    ('7', '8'): '>', ('7', '4'): 'v', 
    ('8', '7'): '<', ('8', '5'): 'v', ('8', '9'): '>', 
    ('9', '8'): '<', ('9', '6'): 'v'
}


dir_pad = nx.DiGraph()
dir_pad.add_edges_from([("A", "^"), ("A", ">")])
dir_pad.add_edges_from([("^", "A"), ("^", "v")])
dir_pad.add_edges_from([("<", "v")])
dir_pad.add_edges_from([("v", "<"), ("v", "^"), ("v", ">")])
dir_pad.add_edges_from([(">", "v"), (">", "A")])

dir_pad_move = {
    ('A', '^'): "<", ('A', '>'): "v",
    ('^', 'A'): ">", ('^', 'v'): "v",
    ('<', 'v'): ">",
    ('v', '<'): "<", ('v', '^'): "^", ('v', '>'): ">",
    ('>', 'v'): "<", ('>', 'A'): "^",
}

def generate_shortest_paths(g, gmove):
    paths = defaultdict(list)
    for s in g.nodes:
        for d in g.nodes:
            if s != d:
                for p in nx.all_shortest_paths(g, s, d):
                    path = []
                    for i in range(len(p) - 1):
                        path.append(gmove[(p[i], p[i+1])])
                    m = "".join(path)
                    paths[(s, d)].append(m)

    return paths
np_shortest = generate_shortest_paths(num_pad, num_pad_move)
dp_shortest = generate_shortest_paths(dir_pad, dir_pad_move)

@cache
def recurse(level, ans, n):
    pad = np_shortest if level == 0 else dp_shortest
    if level == n + 1:
        return len(ans)
    total = 0
    for s,d in zip("A" + ans, ans):
        best = [recurse(level + 1, p + 'A', n) for p in pad[(s,d)]]
        if best:
            total += min(best)
        else:
            total += 1
    return total

p2 = 0
for line in f:
    left = ints(line)
    p2 += recurse(0, line, 25) * left[0]
print(p2)

