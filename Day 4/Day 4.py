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

result = 0
for i in range(4):
    matrix = np.rot90(matrix)
    result += findxmas(matrix)
print(result)