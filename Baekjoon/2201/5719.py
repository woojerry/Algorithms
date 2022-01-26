# 01/26
# 5719 거의 최단 경로
# 다익스트라
# 단일출발/단일도착 최단거리 구하는 문제 + 음수간선X
from collections import deque
import heapq
import sys
read = sys.stdin.readline

INF = int(1e9)

N, M = map(int, read().split())
S, D = map(int, read().split())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    U, V, P = map(int, read().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
