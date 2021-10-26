from collections import deque

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

# 상하좌우 방향키
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    queue = deque()
    queue.append((r, c))

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= n or nc < 0 or nc >= m:  # 미로 밖
                continue

            if graph[nr][nc] == 0:  # 이동할 수 없는 칸
                continue

            if graph[nr][nc] == 1:  # 처음 방문하는 경로일 때
                graph[nr][nc] = graph[r][c] + 1
                queue.append((nr, nc))

    return graph[n-1][m-1]


print(bfs(0, 0))
