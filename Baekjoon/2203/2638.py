# 03/10
# 2638 치즈

from collections import deque
import sys
read = sys.stdin.readline

N, M = map(int, read().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, read().split())))
