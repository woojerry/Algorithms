# 01/25
# 11404 플로이드
# 플로이드-워셜 알고리즘

import sys
read = sys.stdin.readline
INF = int(1e9)

n = int(read())  # 도시의 개수
m = int(read())  # 버스의 개수
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    s, e, c = map(int, input().split())
    if graph[s][e] > c:
        graph[s][e] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()

# print(graph)
