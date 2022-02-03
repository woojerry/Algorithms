# 02/03
# 2206 벽 부수고 이동하기
import copy
import sys
from collections import deque
read = sys.stdin.readline

N, M = map(int, read().split())
graph = []
walls = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(changed_graph):
    queue = deque([(0, 0)])

    while queue:
        r, c = queue.popleft()
        for q in range(4):
            nr = r + dr[q]
            nc = c + dc[q]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if changed_graph[nr][nc] == 'W':
                continue
            if changed_graph[nr][nc] == 0:
                changed_graph[nr][nc] = changed_graph[r][c] + 1
                queue.append((nr, nc))

    return changed_graph[N-1][M-1]


for i in range(N):
    graph.append(list(map(int, read().rstrip())))
    for j in range(M):
        if graph[i][j] == 1:
            walls.append((i, j))
            graph[i][j] = 'W'

answer = 0
for wall in walls:
    a, b = wall
    new_graph = copy.deepcopy(graph)
    new_graph[a][b] = 0

    answer = max(answer, bfs(new_graph))

if answer == 0:
    print(-1)
else:
    print(answer + 1)
