# 12/09
# 14225 부분수열의 합

from itertools import combinations

N = int(input())
answer = 0
num_set = set([])

sequences = list(map(int, input().split()))

for i in range(1, N+1):
    combs = list(combinations(sequences, i))
    for j in combs:
        num_set.add(sum(j))

for k in range(1, 2000000):
    if k not in num_set:
        print(k)
        break
