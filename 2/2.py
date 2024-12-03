import math
levels = []

with open("2/input.txt", "r") as file:
    for line in file:
        levels.append(list(map(int, line.split())))

num_safe_levels = 0

def check_level(level):
    safe = True
    signum = 0
    for i in range(len(level)):
        if i == 0:
            continue
        if i == 1:
            signum = math.copysign(1, level[i] - level[i - 1])
        if math.copysign(1, level[i] - level[i - 1]) != signum:
            safe = False
            break
        if not (1 <= abs(level[i] - level[i - 1]) <= 3):
            safe = False
            break
    return safe

for level in levels:
    safe = check_level(level)
    if safe:
        num_safe_levels += 1
        print(level)
    else:
        for i in range(len(level)):
            level_copy = level[:i] + level[i+1:]
            if check_level(level_copy):
                num_safe_levels += 1
                break

print(num_safe_levels)
