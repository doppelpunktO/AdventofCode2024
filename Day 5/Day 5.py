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

total = 0
for update in updates:
    if all(checkupdate(update, rule) for rule in rules):
        total += update[math.trunc(len(update) / 2)]

print("Part 1:", total)