# Advent of Code 2024 Day 3 - Part 1 & 2
import re

# Part 1:
# get input
data = open("input d3.txt", "r").read()

# filter all important operations
mullist = re.findall(r"mul\(\d{1,3},\d{1,3}\)", data)
list = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", data)

totalp1 = totalp2 = 0
# strip all lines from "mul" and multiply X and Y
for i in mullist:
     i = i.strip("mul()").split(",")
     totalp1 += int(i[0])*int(i[1])

enable = True
# do & donts enable / disable mul function
for i in list:
     if i == "do()" or i == "don't()":
          enable = i == "do()"
     else:
          p = i.strip("mul()").split(",")
          totalp2 += int(p[0]) * int(p[1]) * enable

print("Part 1:", totalp1)
print("Part 2:", totalp2)





