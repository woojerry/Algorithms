# 10/29
# 18352 특정 거리의 도시 찾기 # 단방향 그래프

from collections import deque
import sys
# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호
N, M, K, X = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]  # 0번 인덱스 포함해야하므로 도시의 개수 +1

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)  # 인접노드로 만들기

visited = [False] * (N+1)


def bfs(graph, start, visited):
    cities = []
    queue = deque([(start, 0)])  # deque선언할 때는 iterable
    visited[start] = True

    while queue:
        r, count = queue.popleft()

        if count == K:
            cities.append(r)
            continue

        for i in graph[r]:
            if not visited[i]:
                queue.append((i, count+1))
                visited[i] = True

    return sorted(cities)


answer = bfs(graph, X, visited)
if answer:
    for el in answer:  # print(*bfs, sep='\n')
        print(el)
else:
    print(-1)
