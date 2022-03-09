# 03/09
# 16926 배열돌리기1

import sys
read = sys.stdin.readline

N, M, R = map(int, read().split())  # 반시계
graph = []
for _ in range(N):
    graph.append(list(map(int, read().split())))

for _ in range(R):
    for i in range(min(N, M) // 2):  # i -> depth
        r, c = i, i
        tmp = graph[r][c]

        # 안쪽까지 돌려야하므로 n-i, m-i까지
        for j in range(i+1, N-i):  # 좌
            r = j
            prev_value = graph[r][c]
            graph[r][c] = tmp
            tmp = prev_value

        for j in range(i+1, M-i):  # 하
            c = j
            prev_value = graph[r][c]
            graph[r][c] = tmp
            tmp = prev_value

        for j in range(i+1, N-i):  # 우
            r = N - j - 1
            prev_value = graph[r][c]
            graph[r][c] = tmp
            tmp = prev_value

        for j in range(i+1, M-i):  # 상
            c = M - j - 1
            prev_value = graph[r][c]
            graph[r][c] = tmp
            tmp = prev_value

for i in range(N):
    for j in range(M):
        print(graph[i][j], end=' ')
    print()
