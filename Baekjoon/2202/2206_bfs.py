# 02/03
# 2206 벽 부수고 이동하기
# BFS + 3차원 리스트로 상태관리
import sys
from collections import deque
read = sys.stdin.readline

N, M = map(int, read().split())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]


def bfs():
    # crashed 벽 안부수는 경우: 0, 부수는 경우: 1
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while queue:
        r, c, crashed = queue.popleft()

        if r == N-1 and c == M-1:
            return visited[r][c][crashed]

        for q in range(4):
            nr = r + dr[q]
            nc = c + dc[q]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            # 벽을 부수지 않고 이동하는 경우
            if graph[nr][nc] == 0 and visited[nr][nc][crashed] == 0:
                queue.append((nr, nc, crashed))
                visited[nr][nc][crashed] = visited[r][c][crashed] + 1

            # 벽을 부수고 이동하는 경우
            if graph[nr][nc] == 1 and crashed == 0:
                queue.append((nr, nc, crashed+1))
                visited[nr][nc][crashed + 1] = visited[r][c][crashed] + 1

    return -1


graph = []
for i in range(N):
    graph.append(list(map(int, read().rstrip())))

print(bfs())
print(visited)
