import math
levels = []

with open("2/input.txt", "r") as file:
    for line in file:
        levels.append(list(map(int, line.split())))

num_safe_levels = 0

for level in levels:
    safe = True
    signum = 0
    for i in range(len(level)):
        if i == 0:
            continue
        if i == 1:
            if level[i] > level[i - 1]:
                signum = 1
            elif level[i] < level[i - 1]:
                signum = -1
            else:
                safe = False
                break
        if math.copysign(1, level[i] - level[i - 1]) != math.copysign(1, signum):
            safe = False
            break
        if not (1 <= abs(level[i] - level[i - 1]) <= 3):
            safe = False
            break
    if safe:
        num_safe_levels += 1
        print(level)    

print(num_safe_levels)
