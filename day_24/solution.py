from collections import deque, defaultdict
from utils import ints
from functools import lru_cache
import networkx as nx
import parse as p
import graphviz
f = [x for x in open("mod_input.txt").read().strip().split("\n\n")]

c = defaultdict(int)
for line in f[0].splitlines():
    l,r = line.split(": ")
    r = int(r)
    c[l] = r
# print(c)

# c = defaultdict(int)

def solve_op(s1, op, s2):
    if op == "AND":
        return s1 & s2
    if op == "OR":
        return s1 | s2
    if op == "XOR":
        return s1 ^ s2
while True:
    indexes_hit = set()
    for i, line in enumerate(f[1].splitlines()):
        if i not in indexes_hit:
            s1, op, s2, dest = p.parse("{} {} {} -> {}", line)
            if s1 in c and s2 in c:
                c[dest] = solve_op(c[s1], op, c[s2])
                indexes_hit.add(dest)
    if len(indexes_hit) == len(f[1].splitlines()):
        break
zs = []
for k,v in c.items():
    if k[0] == "z":
        zs.append((k,v))
xs = []
for k,v in c.items():
    if k[0] == "x":
        xs.append((k,v))
ys = []
for k,v in c.items():
    if k[0] == "y":
        ys.append((k,v))

# print(zs)
zs.sort(key=lambda x: x[0], reverse=True)
zs_b = [x[1] for x in zs]
print(zs_b)
ans = 0
for k,v in zs:
    ans = ans * 2 + v
print(ans)
xs.sort(key=lambda x: x[0], reverse=True)
xs_b = [x[1] for x in xs]
print(" ", xs_b)
xans = 0
for k,v in xs:
    xans = xans * 2 + v
# print(xans)
ys.sort(key=lambda x: x[0], reverse=True)
ys_b = [x[1] for x in ys]
print(" ", ys_b)
yans = 0
for k,v in ys:
    yans = yans * 2 + v
print(yans)

carry = 0

print(xans + yans)

added = bin(xans + yans)[2:]
z = bin(ans)[2:]
for i, (l1, l2) in enumerate(zip(added, z)):
    if l2 != l1:
        print(f"mismatch at index: {i}", l1, l2)
print(bin(xans + yans)[2:])
print(bin(ans)[2:])
# 61495910098126 -- z
# 27339360157359 -- x
# 34293989942303 -- y
### for 23, vht is the and of the two
# vph is the xor of the two
# vrw comes from the and of bkg and tgw
# kkq is the and of 22s
# jjr is the or of vrw and kkq
# vph xor jjr makes z23


swaps = ['pqt', 'z37', 'jmv', 'css', 'z05', 'gdd', 'z09', 'cwt']

print(",".join(list(sorted(swaps))))
# z45 is somehow the or of gkb and mgv. it's supposed to be xor --- no it's the carry bit that's fine



# # kvg or sgj makes z09
# # kvg is jnf and wgh
# #        jnf xor wgh makes cwt
# #                          cwt xor wdf makes z10




# # # 37 is one issue
# # # y37 xor x37 makes vcr??? i think it should make z37
# # # vcr is used in: vcr xor nwd to make pqt
# #     
# # 
# # 
# #                                   pqt or dgb makes hjg



# gates = {}
# for line in f[1].splitlines():
#     in_, out = line.split(' -> ')
#     in_ = in_.split()

#     assert out not in gates
#     gates[out] = in_


# def match_against(out, spec):
#     if spec == '*':
#         return set()

#     if out in gates:
#         in_ = gates.get(out)
#         a, op, b = in_
#     else:
#         if spec == out:
#             return set()
#         return {out}

#     if spec[0] != op:
#         return {out}

#     e_ab = match_against(a, spec[1]) | match_against(b, spec[2])
#     e_ba = match_against(b, spec[1]) | match_against(a, spec[2])
#     e = min(e_ab, e_ba, key=len)
#     return e


# zs = [k for k in gates.keys() if k.startswith('z')]
# es = set()
# for z in zs:
#     n = int(z[1:])
#     prev = n-1
#     x_this = z.replace('z', 'x')
#     y_this = z.replace('z', 'y')

#     x_prev = f'x{prev:02d}'
#     y_prev = f'y{prev:02d}'

#     es |= match_against(
#         z,
#         ['XOR',
#            ['XOR', x_this, y_this],
#            ['OR', ['AND', x_prev, y_prev],
#                   ['AND', ['XOR', x_prev, y_prev],
#                           '*']]])

# g = defaultdict(list)
# for out, in_ in gates.items():
#     a, op, b = in_
#     n = f'{a} {op} {b}'
#     g[a].append(n)
#     g[b].append(n)
#     g[n].append(out)

# dot = graphviz.Digraph()

# for node, edges in g.items():
#     for edge in edges:
#         dot.edge(node, edge)

# for e in es:
#     dot.node(e, color='red')

# dot.render('graph_output_v3', format='png')


# # 	z09 [color=red]
# 	vch [color=red]
# 	cwt [color=red]
# 	pqt [color=red]
# 	z05 [color=red]
# 	gdd [color=red]
# 	css [color=red]
# 	z37 [color=red]
# 	jmv [color=red]