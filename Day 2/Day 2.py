# Advent of Code 2024 Day 2 - Part 1 & 2

# get input
data = open("input d2.txt", "r").readlines()

def increasing(line):
    for i in range(0, len(line)-1):
        # if it isn't increasing or two levels differ too much / not at all --> False
        if line[i] >= line[i+1] or line[i] < line[i+1] - 3:
            return False
    return True

def decreasing(line):
    for i in range(0, len(line)-1):
        # if it isn't decreasing or two levels differ too much / not at all --> False
        if line[i] <= line[i+1] or line[i] > line[i+1] + 3:
            return False
    return True
def safe(line):
    return increasing(line) or decreasing(line)
def safe_damper(line):
    if safe(line):
        return True
    else:
        for i in range(len(line)):
            damp_line = line[:i] + line[i+1:]
            if safe(damp_line):
                return True

    return False

countp1 = 0
countp2 = 0

for line in data:
    line = line.split()
    line = [int(i) for i in line]
    # check if "safe"
    if safe(line):
        countp1 += 1
    if safe_damper(line):
        countp2 += 1

print("Part 1:", countp1)
print("Part 2:", countp2)
