# 10/29
# 18405 경쟁적 전염
from collections import deque

N, K = map(int, input().split())


graph = []
info = []
visited = [[False] * N for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int, input().split())))

S, X, Y = map(int, input().split())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

queue = deque()

for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            # 값에 따른 sort
            info.append([graph[i][j], (i, j)])

info.sort(key=lambda x: x[0])

for el in info:
    queue.append((el[1], 0))

while queue:
    (r, c), time = queue.popleft()
    visited[r][c] = True

    for q in range(4):
        nr = r + dr[q]
        nc = c + dc[q]

        if time == S:
            break

        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if graph[nr][nc] == 0 and not visited[nr][nc]:
            graph[nr][nc] = graph[r][c]
            visited[nr][nc] = True
            queue.append(((nr, nc), time+1))


print(graph[X-1][Y-1])
