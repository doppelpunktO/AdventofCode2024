# Advent of Code 2024 Day 5 - Part 1&2
import math
# get input & x
data = open("input d5.txt", "r").readlines()
rules = []
updates = []
# create / seperate input
for index, line in enumerate(data):
    if line == "\n":
        break
    line = line.strip("\n")
    line = line.split("|")
    line = [int(i) for i in line]
    rules.append(line)

for i in range(index+1,len(data)):
    data[i] = data[i].strip("\n")
    data[i] = data[i].split(",")
    data[i] = [int(k) for k in data[i]]
    updates.append(data[i])

def checkupdate(update, rule):
    if rule[0] not in update:
        return True
    for u in update:
        if u == rule[0]:
            return True
        if u == rule[1]:
            return False

def sortupdate(update, rules):

    if all(checkupdate(update, rule) for rule in rules):
        return update
    for rule in rules:
        if checkupdate(update, rule):
            continue
        else:
            i = 0
            for u in update:
                if u == rule[0]:
                    update[i] = rule[1]
                    i += 1
                    continue
                if u == rule[1]:
                    update[i] = rule[0]
                    i += 1
                    continue
                i += 1
    update = sortupdate(update, rules)
    return update


totalp1 = totalp2 = 0
for update in updates:
    if all(checkupdate(update, rule) for rule in rules):
        totalp1 += update[math.trunc(len(update)/2)]
        continue
    # Part 2
    update = sortupdate(update, rules)
    totalp2 += update[math.trunc(len(update)/2)]

print("Part 1:", totalp1)
print("Part 2:", totalp2)