# 03/07
# 9328 열쇠
# BFS + 비트마스킹

from collections import deque
import sys
read = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(read())
for _ in range(T):
    h, w = map(int, read().split())

    graph = [list(read().strip()) for _ in range(h)]

    door = [0] * 26
    keys = list(map(str, read().rstrip()))
    for k in keys:
        if k != '0':
            door[ord(k)-ord('a')] = 1

    for i in range(h):
        for j in range(w):
            if ord('A') <= ord(graph[i][j]) <= ord('Z'):
                if door[ord(graph[i][j]) - ord('A')]:
                    graph[i][j] = '.'

    count = 0

    # 바깥에 '.'로 입구 만들기
    for i in graph:
        i.insert(0, '.')
        i.append('.')
    graph.insert(0, ['.']*(w+2))
    graph.append(['.']*(w+2))

    queue = deque()
    queue.append((0, 0))
    visited = [[False] * (w+2) for _ in range(h+2)]
    visited[0][0] = True

    while queue:
        r, c = queue.popleft()
        visited[r][c] = True
        for q in range(4):
            nr = r + dr[q]
            nc = c + dc[q]

            if nr < 0 or nr >= h+2 or nc < 0 or nc >= w+2:
                continue

            if not visited[nr][nc]:
                if graph[nr][nc] == '.':
                    visited[nr][nc] = True
                    queue.append((nr, nc))

                elif graph[nr][nc].islower():
                    door[ord(graph[nr][nc]) - ord('a')] = 1
                    visited = [[False] * (w+2) for _ in range(h+2)]
                    graph[nr][nc] = '.'
                    queue = deque()
                    queue.append((nr, nc))

                elif graph[nr][nc].isupper():
                    if door[ord(graph[nr][nc]) - ord('A')]:
                        graph[nr][nc] = '.'
                        visited[nr][nc] = True
                        queue.append((nr, nc))

                elif graph[nr][nc] == '$':
                    count += 1
                    visited[nr][nc] = True
                    graph[nr][nc] = '.'
                    queue.append((nr, nc))

    print(count)
