# 1/3
# 16932 모양 만들기
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(i, j, idx):
    cnt = 1
    queue = deque()
    queue.append((i, j))
    graph[i][j] = -1
    visited[i][j] = idx

    while queue:
        r, c = queue.popleft()
        for q in range(4):
            nr = r + dr[q]
            nc = c + dc[q]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if graph[nr][nc] == 1:
                visited[nr][nc] = idx  # visited의 값을 인덱스로
                graph[nr][nc] = -1  # 이미 방문한 것 -1로
                queue.append((nr, nc))
                cnt += 1
    return cnt  # 이어져 있는 횟수 cnt


N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

idx = 1
visited = [[0] * M for _ in range(N)]
group = {}
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            cnt = bfs(i, j, idx)
            group[idx] = cnt  # 각각 이어져 있는 횟수 저장
            idx += 1

answer = 0
for r in range(N):
    for c in range(M):
        if graph[r][c] == 0:
            ss = set()
            for s in range(4):  # 0에서 인접한 칸 방문
                nr = r + dr[s]
                nc = c + dc[s]

                if nr < 0 or nr >= N or nc < 0 or nc >= M:
                    continue
                if graph[nr][nc] == -1:
                    ss.add(visited[nr][nc])

            sums = 1  # 0에서 1되는 것
            for k in ss:
                sums += group[k]

            answer = max(answer, sums)

print(answer)
