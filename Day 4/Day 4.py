# Advent of Code 2024 Day 4 - Part 1 & 2
import re
import numpy as np
# get input
input = np.loadtxt("input d4.txt", dtype=str)
matrix = np.array([list(word) for word in input])

regex = r"XMAS"
def findxmas(matrix):
    result = 0
    # check amount of XMAS in horizontal row
    for line in matrix:
        string = ""
        for word in line:
            string += word
        result += len(re.findall(regex, string))
    # check amount of XMAS in diagonal row
    for i in range(len(matrix)):
        string = ""
        for n in range(len(matrix[1])-i):
            string += matrix[n+i,n]
        result += len(re.findall(regex, string))


    for i in reversed(range(1, len(matrix))): # col
        string  = ""
        for n in range(len(matrix[1])-i): # row
            string += matrix[n,i+n]
        result += len(re.findall(regex, string))

    return result

resultp1 = 0
for i in range(4):
    matrix = np.rot90(matrix)
    resultp1 += findxmas(matrix)
print("Part 1:", resultp1)

# Part 2
regexp2 = r'M.M.A.S.S|M.S.A.M.S|S.M.A.S.M|S.S.A.M.M'
# find if line == X-MAS
resultp2 = 0

for i in range(len(matrix[0])-2):
    for n in range(len(matrix[1])-2):
        line = ""
        for c in range(3):
            for d in range(3):
                line += (matrix[i+c,n+d])
        print(line)
        if re.match(regexp2, line):
            resultp2 += 1

print("Part 2:", resultp2)

