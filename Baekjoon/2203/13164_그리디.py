# 03/15
# 13164 행복유치원

import sys
read = sys.stdin.readline

N, K = map(int, read().split())
heights = list(map(int, read().split()))

costs = []
for i in range(1, N):
    costs.append(heights[i] - heights[i-1])

costs.sort()

answer = 0

if K != 0:
    for i in range(N-K):
        answer += costs[i]

print(answer)
