f = [x for x in open("input.txt").read().strip().split("\n\n")]

parts = f[0].strip().split(", ")
lines = f[1].strip().split("\n")


def can_form_string(substrings, target):
    from functools import lru_cache

    @lru_cache(None)
    def helper(remaining):

        if not remaining:
            return 1
        total = 0
        for sub in substrings:
            if remaining.startswith(sub): 
                total += helper(remaining[len(sub):]) 
        return total

    return helper(target)


p1 = 0
p2 = 0
for line in lines:
    ways = can_form_string(parts, line)
    if ways > 0:
        p1 += 1
    p2 += ways
print(p1)
print(p2)

