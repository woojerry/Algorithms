# 03/01
# 1005 ACM CRAFT
from collections import deque
import sys
read = sys.stdin.readline

T = int(read())
for _ in range(T):
    N, K = map(int, read().split())
    graph = [[] for _ in range(N+1)]
    indgree = [0] * (N+1)
    
    D = [0] + list(map(int, read().split()))
    for _ in range(K):
        X, Y = map(int, read().split())
        graph[X].append(Y)
        indgree[Y] += 1
        
    W = int(read())
        
    queue = deque()
    for i in range(1, N+1):
        if indgree[i] == 0:
            queue.append((i, D[i]))
            
    cost = [0] * (N+1)
    for i in range(1, N+1):
        cost[i] = D[i]
        
    while queue:
        now, previous_cost = queue.popleft()
        if now == W:
            break
        for i in graph[now]:
            indgree[i] -= 1
            # 다른 것들이 다 지어져야 다음 건물이 지어질 수 있으므로
            cost[i] = max(cost[i], previous_cost + D[i]) 
            if indgree[i] == 0:
                queue.append((i, cost[i]))
                
    print(graph)
    
    print(cost[W])