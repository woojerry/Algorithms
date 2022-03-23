# 03/23
# 2638 치즈

from collections import deque
import sys
read = sys.stdin.readline
global graph
global N, M


def bfs():
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    visited = [[False] * M for _ in range(N)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    cheese_count = 0

    while queue:
        r, c = queue.popleft()
        for q in range(4):
            nr = r + dr[q]
            nc = c + dc[q]

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if graph[nr][nc] == 0:
                    visited[nr][nc] = True
                    queue.append((nr, nc))

                elif graph[nr][nc] == 1:
                    graph[nr][nc] = 0
                    cheese_count += 1
                    visited[nr][nc] = True

    return cheese_count


N, M = map(int, read().split())
graph = []
for i in range(N):
    graph.append(list(map(int, read().split())))

time = 0
while True:
    time += 1
    cnt = bfs()
    print(cnt)
    if cnt == 0:
        break

print(time-1)
