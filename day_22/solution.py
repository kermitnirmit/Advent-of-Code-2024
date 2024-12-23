from collections import deque, defaultdict
from utils import ints
from functools import lru_cache
import networkx as nx
f = [x for x in open("input.txt").read().strip().split("\n")]
c = 0

# In particular, each buyer's secret number evolves into the next secret number in the sequence via the following process:

# Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret number. Finally, prune the secret number.
# Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer. Then, mix this result into the secret number. Finally, prune the secret number.
# Calculate the result of multiplying the secret number by 2048. Then, mix this result into the secret number. Finally, prune the secret number.
# Each step of the above process involves mixing and pruning:

# To mix a value into the secret number, calculate the bitwise XOR of the given value and the secret number. Then, the secret number becomes the result of that operation. (If the secret number is 42 and you were to mix 15 into the secret number, the secret number would become 37.)
# To prune the secret number, calculate the value of the secret number modulo 16777216. Then, the secret number becomes the result of that operation. (If the secret number is 100000000 and you were to prune the secret number, the secret number would become 16113920.)
m = defaultdict(list)
c = 0
for ind, line in enumerate(f):
    prev = ints(line)[0]
    prev_price = prev % 10
    changes = deque([])
    seen = set()
    for _ in range(2000):
        prev = ((prev * 64) ^ prev) % 16777216
        prev = ((prev // 32) ^ prev ) % 16777216
        prev = ((prev * 2048) ^ prev) % 16777216
        new_price = prev % 10
        changes.append(new_price - prev_price)
        if len(changes) == 5:
            changes.popleft()
        # print(changes, new_price, prev)
        if tuple(changes) not in seen and len(changes) == 4:
            seen.add(tuple(changes))
            m[tuple(changes)].append((ind, new_price)) # best result from this monkey
        prev_price = new_price

    # print(ints(line)[0], prev)
    c += prev
print(c)


max_sum = 0
k_with_max_sum = None
for k, v in m.items():
    n_sum = sum(x[1] for x in v)
    max_sum = max(max_sum, n_sum)
    if n_sum == max_sum:
        k_with_max_sum = k

print(max_sum)