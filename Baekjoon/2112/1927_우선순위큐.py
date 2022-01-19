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
        if len(h) == 0:  # 배열이 비어있는 경우
            print(0)
        else:  # 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거
            print(heapq.heappop(h))

    else:
        heapq.heappush(h, x)
