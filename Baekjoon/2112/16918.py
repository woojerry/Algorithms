# 12/30
# 16918 봄버맨
from collections import deque


def find_bomb():
    for i in range(R):
        for j in range(C):
            if graph[i][j] == 'O':
                queue.append((i, j))


def set_bomb():
    for i in range(R):
        for j in range(C):
            if graph[i][j] != 'O':
                graph[i][j] = 'O'


def boom():
    while queue:
        dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
        r, c = queue.popleft()
        graph[r][c] = '.'
        for q in range(4):
            nr = r + dr[q]
            nc = c + dc[q]

            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                continue
            if graph[nr][nc] == 'O':
                graph[nr][nc] = '.'


R, C, N = map(int, input().split())


queue = deque([])
others = []
graph = [list(input()) for _ in range(R)]


N -= 1  # 1초 동안 봄버맨은 아무것도 하지 않는다.
while N != 0:
    find_bomb()
    set_bomb()
    N -= 1
    if N == 0:
        break
    boom()
    N -= 1

for i in range(R):
    for j in range(C):
        print(graph[i][j], end='')
    print()
