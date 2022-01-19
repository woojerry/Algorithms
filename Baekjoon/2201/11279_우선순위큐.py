# 01/19
# 11279 최대 힙

import sys
import heapq
read = sys.stdin.readline

N = int(read())
h = []

for _ in range(N):
    x = int(read())
    if x == 0:
        if len(h) == 0:
            print(0)
        else:
            print(-1 * heapq.heappop(h))  # 꺼낼 때 -1 다시 곱해 양수로

    else:
        heapq.heappush(h, -x)  # 파이썬은 최소힙으로 돼있으므로 음수값으로 넣어준뒤
