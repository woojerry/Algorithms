from collections import deque
import sys
read = sys.stdin.readline

N, M = map(int, read().split())
graph = [[] for _ in range(N+1)]
indgree = [0] * (N+1)

for _ in range(M):
    A, B = map(int, read().split())
    graph[A].append(B)
    indgree[B] += 1
    
queue = deque()
for i in range(1, N+1):
    if indgree[i] == 0:
        queue.append((i, 1))

dp = [1] * (N+1)

while queue:
    now, cost = queue.popleft()
    
    for i in graph[now]:
        indgree[i] -= 1
        
        dp[i] = max(dp[i], cost + 1)
        if indgree[i] == 0:
            queue.append((i, dp[i]))

for i in range(1, N+1):
    print(dp[i], end=' ')