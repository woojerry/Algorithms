# 10/28
# 7576 토마토

from collections import deque

M, N = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

queue = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))

while queue:
    r, c = queue.popleft()

    for q in range(4):
        nr = r + dr[q]
        nc = c + dc[q]

        if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] == 0:
            graph[nr][nc] = graph[r][c] + 1
            queue.append((nr, nc))


def answer():
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:  # 토마토가 모두 익지 못하는 상황
                print(-1)
                return

    print(max(map(max, graph)) - 1)  # 2차원 리스트 최댓값 map 이용


answer()
