# Advent of Code Day 1 - Part 1 & 2

# import lists
data = open("Day 1\locationIDs.txt", "r")
list = data.read().split()
list = [int(i) for i in list]
data.close()
# split lists
l1 = list[::2]
l2 = list [1::2]
# sort lists
sortl1 = sorted(l1)
sortl2 = sorted(l2)

total = 0
# dictionary & counter for P2
sim = 0
simdic = {}
for i in range(0,len(sortl1)):
    if sortl1[i] in sortl2:
        # look how many appearences i has in l2
        c = sortl2.count(sortl1[i])
        simdic[sortl1[i]] = c
    # add every distance to total
    total += abs(sortl1[i] - sortl2[i])
# multiply all similarities
for i in simdic:
    sim += i * simdic[i]
print(total, sim)


