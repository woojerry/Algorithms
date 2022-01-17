# 01/07
# 3055 탈출
from collections import deque
import pprint

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(input()))

waters = []
start = (0, 0)
queue = deque()
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'D':
            end = (i, j)
        elif graph[i][j] == 'S':
            start_i, start_j = i, j
        elif graph[i][j] == '*':
            queue.append((i, j, 0))  # 물 넣기

visited = [[False for _ in range(C)] for _ in range(R)]  # 고슴도치의 이동위치 표기를 위해
queue.append((start_i, start_j, 0))  # 고슴도치 넣기
visited[start_i][start_j] = True
success = False


while queue:
    r, c, count = queue.popleft()

    for q in range(4):
        nr = r + dr[q]
        nc = c + dc[q]
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            continue

        if graph[r][c] == '*':  # 물일 경우
            if graph[nr][nc] == '.':
                graph[nr][nc] = '*'
                queue.append((nr, nc, count + 1))

        elif graph[r][c] == 'S':  # 고슴도치일 경우
            if not visited[nr][nc]:
                if graph[nr][nc] == '*':
                    continue
                if graph[nr][nc] == 'D':
                    success = True
                    break
                if graph[nr][nc] == '.':
                    queue.append((nr, nc, count + 1))
                    graph[nr][nc] = 'S'
                    visited[nr][nc] = True

    if success:
        break

if success:
    print(count+1)
else:
    print('KAKTUS')
