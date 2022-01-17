# 10/28
# 7576 토마토
# BFS

from collections import deque

M, N = map(int, input().split())
graph = []
tomatoes = []

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
visited = [[False] * M for _ in range(N)]

count = 0
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(M):
        if graph[i][j] == 1:
            visited[i][j] == True
            tomatoes.append((i, j, count))


queue = deque(tomatoes)
while queue:
    r, c, count = queue.popleft()

    for q in range(4):
        nr = r + dr[q]
        nc = c + dc[q]

        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        if graph[nr][nc] == 0:
            visited[nr][nc] == True
            queue.append((nr, nc, count+1))
            graph[nr][nc] = 1


flag = False
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            flag = True
            print(-1)
            break
    if flag:
        break
if not flag:
    print(count)
