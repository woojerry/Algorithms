# 03/25
from collections import deque


def solution(n, edge):
    answer = 0

    graph = [[] for _ in range(n+1)]
    distance = [0] * (n+1)
    visited = [False] * (n+1)

    for e in edge:
        a, b = e
        graph[a].append(b)
        graph[b].append(a)

    queue = deque([1])
    visited[1] = True
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                distance[i] = distance[now] + 1
                queue.append(i)
                visited[i] = True

    max_distance = max(distance)
    for i in range(1, n+1):
        if distance[i] == max_distance:
            answer += 1

    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
