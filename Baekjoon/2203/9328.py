# 03/03
# 9328 열쇠

from collections import deque
from pprint import pprint
import sys
read = sys.stdin.readline


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(read())
for _ in range(T):
    h, w = map(int, read().split())
    graph = []
    for _ in range(h):
        graph.append(list(map(str, read())))

    tmp = read()
    if tmp == '0':
        keys = []
    else:
        keys = list(map(str, tmp))

    queue = deque()
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '.':
                if i == 0 or i == h-1 or j == 0 or j == w-1:
                    queue.append((i, j))
            elif graph[i][j].isupper() and graph[i][j].lower() in keys:
                graph[i][j] = '.'

    visited = [[False] * w for _ in range(h)]
    while queue:
        r, c = queue.popleft()
        visited[r][c] = True
        for q in range(4):
            nr = r + dr[q]
            nc = c + dc[q]

            if nr < 0 or nr >= h or nc < 0 or nc >= w:
                continue
            if not visited[nr][nc]:
                if graph[nr][nc] == '*':
                    continue
                elif graph[nr][nc] == '.':
                    queue.append((nr, nc))

                elif graph[nr][nc].islower():
                    keys.append(graph[nr][nc])
                    visited = [[False] * w for _ in range(h)]
                    graph[nr][nc] = '.'
                    queue.append((nr, nc))

                elif graph[nr][nc].isupper():
                    if graph[nr][nc].lower() in keys:
                        graph[nr][nc] = '.'
                        queue.append((nr, nc))

    print(keys)
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '.':
                if i == 0 or i == h-1 or j == 0 or j == w-1:
                    queue.append((i, j))
                elif graph[i][j].isupper() and graph[i][j].lower() in keys:
                    graph[i][j] = '.'

    pprint(graph)

    visited = [[False] * w for _ in range(h)]
    count = 0
    while queue:
        r, c = queue.popleft()
        visited[r][c] = True
        for q in range(4):
            nr = r + dr[q]
            nc = c + dc[q]

            if nr < 0 or nr >= h or nc < 0 or nc >= w:
                continue
            if not visited[nr][nc]:
                if graph[nr][nc] == '*':
                    continue
                elif graph[nr][nc] == '.':
                    queue.append((nr, nc))
                elif graph[nr][nc] == '$':
                    count += 1
                    graph[nr][nc] == '.'
                    queue.append((nr, nc))
    # pprint(graph)
    # elif graph[nr][nc] == '$':
    #     count += 1
    #     graph[nr][nc] = '.'

    print(count)
    # pprint(graph)
