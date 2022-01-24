# 01/24
# 2252 줄세우기
# 위상정렬

from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
queue = deque()

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)

result = []
while queue:
    now = queue.popleft()
    result.appned(now)

    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append(i)

for i in result:
    print(i, end=' ')
