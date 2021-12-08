# 12/08
# 1927 최소 힙
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
            print(heapq.heappop(h))

    else:
        heapq.heappush(h, x)
