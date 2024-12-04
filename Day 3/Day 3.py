# Advent of Code 2021 Day 3 - Part 1 & 2
import re

# Part 1:
# get input
datap1 = open("input d3.txt", "r").read()

# filter all mul operations
mullist = re.findall(r"mul\(\d{1,3},\d{1,3}\)", datap1)

# strip all lines from "mul" and multiply X and Y
totalp1 = 0
for i in mullist:
     i = i.strip("mul()").split(",")
     totalp1 += int(i[0])*int(i[1])

print("Part 1:", totalp1)

# Part 2
# get input
datap2 = open("input d3 p2.txt", "r").read()

# Patterns for do's and don't's
dopatt = re.compile(r"do\(\)")
dontpatt = re.compile(r"don't\(\)")
enable = 0