# 12/4
# 2512 예산
import sys

read = sys.stdin.readline
N = int(read())
requests = list(map(int, read().split()))
M = int(read())

start, end = 0, max(requests)  # start는 0으로 ..
answer = 0

while start <= end:
    mid = (start + end) // 2
    budget = 0
    for request in requests:
        budget += min(request, mid)
    if budget > M:
        end = mid - 1

    else:
        answer = mid
        start = mid + 1

print(answer)
