# Advent of Code 2024 Day 5 - Part 1&2

# get input & x
data = open("input d5.txt", "r").readlines()
rules = []
updates = []

for index, line in enumerate(data):
    if line == "\n":
        break
    line = line.strip("\n")
    line = line.split("|")
    rules.append(line)

for i in range(index+1,len(data)):
    data[i] = data[i].strip("\n")
    data[i] = data[i].split(",")
    updates.append(data[i])
for list in updates:
    list = (int(i) for i in list)

print(rules)
print(updates)
print(index)