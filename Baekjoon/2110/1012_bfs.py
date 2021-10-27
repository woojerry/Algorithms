# 10/27
# 유기농 배추

from collections import deque

T = int(input())  # 테스트 케이스 개수

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * N for _ in range(M)]

    for _ in range(K):
        R, C = map(int, input().split())
        graph[R][C] = 1

    visited = [[0] * N for _ in range(M)]
    answer = 0

    def bfs(r, c):
        queue = deque()
        queue.append((r, c))

        visited[r][c] = 1

        while queue:
            r, c = queue.popleft()
            for q in range(4):
                nr = r + dr[q]
                nc = c + dc[q]

                if nr < 0 or nr >= M or nc < 0 or nc >= N:
                    continue
                if graph[nr][nc] == 0:
                    continue
                if graph[nr][nc] == 1 and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))
        return

    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
                answer += 1
    print(answer)
