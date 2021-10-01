# DFS 함수 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:  # 인접 노드가 방문되지 않은 상태라면
            dfs(graph, i, visited)


# 각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
    [],  # 0번 index를 위한 빈 리스트
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9  # 0번 index 때문에 9개로 초기화

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)

print(dfs)  # 1 2 7 6 8 3 4 5
