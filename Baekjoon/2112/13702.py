# 12/27
# 13702 이상한 술집
import sys
read = sys.stdin.readline

N, K = map(int, read().split())  # N <= K
drinks = [int(read()) for _ in range(N)]

start, end = 1, max(drinks)

while start <= end:
    count = 0
    mid = (start + end) // 2

    for i in drinks:
        count += i // mid

    if count < K:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid

print(answer)
