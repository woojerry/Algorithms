# 11/02
# 18428 감시 피하기
from collections import deque
from itertools import combinations
import copy

N = int(input())
init_graph = []
blank_list = []
teacher_list = []

for i in range(N):
    init_graph.append(list(map(str, input().split())))
    for j in range(N):
        if init_graph[i][j] == "T":
            teacher_list.append((i, j))
        elif init_graph[i][j] == "X":
            blank_list.append((i, j))


def bfs(graph):
    queue = deque(teacher_list)
    found = False

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        r, c = queue.popleft()
        for q in range(4):
            nr = r + dr[q]
            nc = c + dc[q]
            while True:  # 그 방향으로 계속 탐색
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    break
                if graph[nr][nc] == "O":
                    break
                if graph[nr][nc] == "S":
                    found = True
                    return found
                nr = nr + dr[q]
                nc = nc + dc[q]
    return found


for el in combinations(blank_list, 3):
    new_graph = copy.deepcopy(init_graph)
    for (r, c) in el:
        new_graph[r][c] = "O"

    if bfs(new_graph) == False:
        print("YES")
        exit()

print("NO")
