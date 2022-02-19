from cmath import cos
from collections import deque
import queue

def solution(value, projects):
    n = len(value)

    indegree = [0] * n
    dp = [0] * n
    q = deque()

    for x, y in projects:
        #print(x,y)
        indegree[x-1] += 1
    
    #print(indegree)

    for i in range(n):
        if indegree[i] == 0:
            q.append((i, value[i]))

    for i in range(n):
        dp[i] = value[i]
    
    print(q)
    while q:
        node, cost = q.popleft()
        print(node, cost)
        node -= 1
        print(projects)
        print(projects[node])
        print(node)
        for next in projects[node]:
            #print(next)
            next -= 1
            indegree[next] -= 1
            dp[next] = max(dp[next], cost + value[next])
            if indegree[next] == 0:
                q.append((next, dp[next]))
    # print(dp)
                
    return dp[0]

print(solution([10, 11, 8, 5, 9, 15, 17], [[1,2],[1,3],[1,4],[3,5],[3,6], [4,7]]))