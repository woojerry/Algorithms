# 11/05
# 2309 일곱 난쟁이

# Combination Ver.
from itertools import combinations

dwarf = []
for _ in range(9):
    dwarf.append(int(input()))

cands = list(combinations(dwarf, 7))

answer = []
for i in cands:
    if sum(i) == 100:
        for j in i:
            answer.append(j)
        break

for k in sorted(answer):
    print(k)

# ------------------------------------------
# Brute Force Ver.

dwarf = []
for _ in range(9):
    dwarf.append(int(input()))

dwarf.sort()
heights_sum = sum(dwarf)
for i in range(len(dwarf) - 1):
    for j in range(i+1, len(dwarf)):
        #print((i, j))
        if heights_sum - dwarf[i] - dwarf[j] == 100:
            for k in range(9):
                if k == i or k == j:
                    continue
                else:
                    print(dwarf[k])
            exit()
