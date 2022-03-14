# 03/09
# 16935 배열 돌리기3
import sys

global N, M, R
global graph

read = sys.stdin.readline

N, M, R = map(int, read())
graph = []
for _ in range(N):
    graph.append(list(map(int, read().split())))

calculate = int(read())
for _ in range(R):
    if calculate == 1:
        ddd
