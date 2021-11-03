# 11/02
# 2606 바이러스 # 양방향 그래프
from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(int(input())):
    a, b = map(int, input().split())  # 인접노드 만들기
    graph[a].append(b)
    graph[b].append(a)


visited = [False] * (N+1)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    nodes = []
    while queue:
        q = queue.popleft()
        nodes.append(q)

        for i in graph[q]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    print(len(list(set(nodes))) - 1)  # 1은 제외
    return


bfs(graph, 1, visited)
