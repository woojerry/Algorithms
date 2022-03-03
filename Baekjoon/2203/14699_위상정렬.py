# 03/03
# 14699 관악산 등산

from collections import deque
import sys
read = sys.stdin.readline

N, M = map(int, read().split())
heights = list(map(int, read().split()))

graph = [[] for _ in range(N+1)]
indgree = [0] * (N+1)

for _ in range(M):
    A, B = map(int, read().split())
    if heights[A-1] >= heights[B-1]:
        graph[A].append(B)
        indgree[B] += 1
    else:
        graph[B].append(A)
        indgree[A] += 1

queue = deque()
dp = [1] * (N+1)


for i in range(1, N+1):
    if indgree[i] == 0:
        queue.append((i, 1))

while queue:
    now, cost = queue.popleft()

    for i in graph[now]:
        indgree[i] -= 1

        dp[i] = max(dp[i], cost+1)
        if indgree[i] == 0:
            queue.append((i, dp[i]))

for i in range(1, N+1):
    print(dp[i])
