# 12/03
# 2805 나무 자르기
# 이분탐색

import sys
read = sys.stdin.readline

N, M = map(int, read().split())
trees = list(map(int, read().split()))

start, end = 0, max(trees)

while start <= end:
    sums = 0
    mid = (start + end) // 2
    # for tree in trees:
    #     if tree > mid:
    #         sum += tree - mid
    sums = sum([tree-mid if tree > mid else 0 for tree in trees])

    if sums < M:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)
