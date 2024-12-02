# Advent of Code 2024 Day 2 - Part 1 & 2

# get input
data = open("Day 2\input d2.txt", "r").readlines()

def increasing(line):
    dampener = 0
    for i in range(0, len(line)-1):
        # if it isn't increasing or two levels differ too much / not at all --> False
        if line[i] > line[i+1-dampener] or line[i] < line [i+1-dampener] - 3 or line[i] == line [i+1-dampener]: # line[i] == line [i+1-dampener] wrong, but don't know how to fix
            # added for P2
            dampener += 1
            line.pop(i)
            if dampener > 1:
                return False 
    return True

def decreasing(line):
    dampener = 0
    for i in range(0, len(line)-1):
        # if it isn't decreasing or two levels differ too much / not at all --> False
        if line[i] == line [i+1] and dampener == 0:
            dampener += 1
            line.pop(i)
        
        if line[i] < line[i+1-dampener] or line[i] > line [i+1-dampener] + 3 or line[i] == line [i+1-dampener]: # line[i] == line [i+1-dampener] wrong, but don't know how to fix
            # added for P2
            dampener += 1
            line.pop(i)
            if dampener > 1:
                return False
        
    return True

count = 0

for line in data:
    line = line.split()
    line = [int(i) for i in line]
    # check if "safe"
    if decreasing(line) or increasing(line):
        count += 1

print(count)
