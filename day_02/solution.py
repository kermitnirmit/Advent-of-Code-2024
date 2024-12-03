f = [x.strip() for x in open("input.txt").readlines()]

f = [[int(x) for x in line.split(" ")] for line in f]
print(f)


def is_safe(line):
    if all(1 <= b-a <= 3 for a,b in zip(line, line[1:])) and line[-1] > line[0]:
        return True
    elif all(-3 <= b-a <= -1 for a,b in zip(line, line[1:])) and line[-1] < line[0]:
        return True
    return False


c = 0
for line in f:
    if is_safe(line):
        c += 1
    else:
        for i in range(len(line)):
            n_line = line[:i] + line[i+1:]
            if is_safe(n_line):
                c += 1
                break
print(c)


