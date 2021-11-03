# 10/26
# 2667 단지번호붙이기
from collections import deque

N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

visited = [[0] * N for _ in range(N)]


def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    cnt = 1  # 방문 안된 집이 있는 곳에서 시작하므로
    visited[r][c] = 1

    while queue:
        r, c = queue.popleft()
        for q in range(4):
            nr = r + dr[q]
            nc = c + dc[q]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            if graph[nr][nc] == 0:
                continue

            if graph[nr][nc] == 1 and visited[nr][nc] == 0:  # 집이 있고, 방문을 한적이 없으면
                visited[nr][nc] = 1
                queue.append((nr, nc))
                cnt += 1
    return cnt


answer = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:
            answer.append(bfs(i, j))

answer.sort()
print(len(answer))
for k in range(len(answer)):
    print(answer[k])
