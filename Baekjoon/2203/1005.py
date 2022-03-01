# 03/01
# 1005 ACM 
from collections import deque
import sys
from time import time
read = sys.stdin.readline

T = int(read())
for _ in range(T):
    N, K = map(int, read().split())
    graph = [[] for _ in range(N+1)]
    indgree = [0] * (N+1)
    
    D = list(map(int, read().split()))
    for _ in range(K):
        X, Y = map(int, read().split())
        graph[X].append(Y)
        indgree[Y] += 1
        
    W = int(read())
        
    queue = deque()
    for i in range(1, N+1):
        if indgree[i] == 0:
            queue.appned(i, D[i])
            
    cost = [0] * (N+1)
    for i in range(1, N+1):
        cost[i] = D[i]
        
    while queue:
        now, time = queue.popleft()
        if now == W:
            break
        for i in graph[now]:
            indgree[i] -= 1
            cost[i] = max(cost[i], time + D[i]) 
            if indgree[i] == 0:
                queue.appned(i, cost[i])
    
    print(cost[W])