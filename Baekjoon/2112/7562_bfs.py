# 12/29
# 7562 나이트의 이동

from collections import deque

T = int(input())

for _ in range(T):
    I = int(input())  # 체스판 한 변의 길이
    graph = [[0] * I for _ in range(I)]
    current_X, current_Y = map(int, input().split())
    move_X, move_Y = map(int, input().split())
    answer = 0

    dr = [-1, -2, -2, -1, 1, 2, 2, 1]
    dc = [2, 1, -1, -2, -2, -1, 1, 2]

    queue = deque([(current_X, current_Y)])
    while queue:
        r, c = queue.popleft()
        if r == move_X and c == move_Y:
            answer = graph[r][c]
            break
        for q in range(8):
            nr = r + dr[q]
            nc = c + dc[q]
            if nr < 0 or nr >= I or nc < 0 or nc >= I:
                continue
            if graph[nr][nc] == 0:
                graph[nr][nc] = graph[r][c] + 1
                queue.append((nr, nc))

    print(answer)
