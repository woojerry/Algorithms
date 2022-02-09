# 01/19
# 1202 보석 도둑
# 우선순위 큐를 사용해 O(N^2) -> O(NlogN)
# 우선순위 큐 + 그리디

import sys
import heapq
read = sys.stdin.readline

N, K = map(int, read().split())
gems, bags = [], []
for _ in range(N):
    M, V = map(int, read().split())
    heapq.heappush(gems, (M, V))
for _ in range(K):
    bags.append(int(read()))

print()
bags.sort()
answer = 0
h = []

for bag in bags:  # 가방 작은 것부터
    while gems:
        if bag >= gems[0][0]:
            weight, price = heapq.heappop(gems)
            heapq.heappush(h, -price)

        else:
            break

    if len(h) > 0:
        answer -= heapq.heappop(h)
    elif len(gems) == 0:
        break

print(answer)
