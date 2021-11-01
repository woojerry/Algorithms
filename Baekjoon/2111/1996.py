# 11/01
# 1996 지뢰 찾기

N = int(input())

graph = []
answer = [[0] * N for _ in range(N)]
for _ in range(N):
    graph.append(list(map(str, input())))

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

for r in range(N):
    for c in range(N):
        for k in range(8):
            nr = r + dr[k]
            nc = c + dc[k]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            if graph[nr][nc] != '.':
                answer[r][c] += int(graph[nr][nc])
        if answer[r][c] >= 10:
            answer[r][c] = 'M'

for i in range(N):
    for j in range(N):
        if graph[i][j] != '.':
            answer[i][j] = '*'

for i in range(N):
    for j in range(N):
        print(answer[i][j], end='')
    print("")
