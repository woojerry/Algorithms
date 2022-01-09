# 01/09
# 11559 Puyo Puyo
# bfs + 구현
from pprint import pprint
from collections import deque

graph = []

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(i, j):
    burst = False
    visited = [[False] * 6 for _ in range(12)]
    queue = deque()
    queue.append((i, j))

    bursted = []
    puyo = 1
    while queue:
        r, c = queue.popleft()
        bursted.append((r, c))
        visited[r][c] = True

        for q in range(4):
            nr = r + dr[q]
            nc = c + dc[q]
            if nr < 0 or nr >= 12 or nc < 0 or nc >= 6:
                continue
            if graph[nr][nc] == graph[r][c] and not visited[nr][nc]:
                queue.append((nr, nc))
                bursted.append((nr, nc))
                visited[nr][nc] = True
                puyo += 1

    if puyo >= 4:
        burst = True
        for br, bc in bursted:
            graph[br][bc] = '.'

    return burst


def gravity():
    for c in range(6):
        queue = deque()
        for r in range(12):
            if graph[11-r][c] != '.':
                queue.append(graph[11-r][c])
        for r in range(12):
            if queue:
                graph[11-r][c] = queue.popleft()
            else:
                graph[11-r][c] = '.'


answer = 0
for i in range(12):
    graph.append(list(input()))

while True:
    chain = False
    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.':
                if bfs(i, j):
                    chain = True

    # pprint(graph)
    if not chain:
        break
    else:  # 연쇄 일어났을 때
        answer += 1
        gravity()


print(answer)
