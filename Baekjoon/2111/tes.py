# 11/03
# 14502 연구소
from collections import deque
from itertools import combinations
import copy

N, M = map(int, input().split())
init_graph = []
blank_list = []
virus_list = []

for i in range(N):
    init_graph.append(list(map(int, input().split())))
    for j in range(M):
        if init_graph[i][j] == 0:
            blank_list.append((i, j))
        elif init_graph[i][j] == 2:
            virus_list.append((i, j))
# print(init_graph)


def bfs(graph):
    queue = deque(virus_list)

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        r, c = queue.popleft()
        for q in range(4):
            nr = r + dr[q]
            nc = c + dc[q]

            if 0 <= nr < N and 0 <= nc < M:
                # if graph[nr][nc] == 1:
                #     continue
                if graph[nr][nc] == 0:
                    graph[nr][nc] = 2
                    queue.append((nr, nc))

    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt += 1
    return cnt


answer = 0
for el in combinations(blank_list, 3):
    new_graph = copy.deepcopy(init_graph)
    for (r, c) in el:
        new_graph[r][c] = 1
        answer = max(answer, bfs(new_graph))

# print(safe_list)
print(answer)
