# 03/08
# 1516 게임 개발
# 위상정렬

from collections import deque
import sys
read = sys.stdin.readline

N = int(read())  # 건물의 수

graph = [[] for _ in range(N+1)]
indgree = [0] * (N+1)
dp = [0] * (N+1)
time = [0] * (N+1)

for i in range(N):
    _input = list(map(int, read().split()))
    time[i+1], vertexes = _input[0], _input[1:]
    for b in vertexes:
        if b == -1:
            break
        else:
            graph[b].append(i+1)
            indgree[i+1] += 1

queue = deque()
for i in range(1, N+1):
    if indgree[i] == 0:
        queue.append((i, time[i]))

for i in range(1, N+1):
    dp[i] = time[i]

while queue:
    now, cost = queue.popleft()

    for i in graph[now]:
        indgree[i] -= 1

        dp[i] = max(dp[i], cost + time[i])
        if indgree[i] == 0:
            queue.append((i, dp[i]))

for i in range(1, N+1):
    print(dp[i])
