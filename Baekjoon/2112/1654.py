# 12/3
# 1654 랜선 자르기
import sys
read = sys.stdin.readline

K, N = map(int, read().split())
cables = [int(read()) for _ in range(K)]
start, end = 1, max(cables)
answer = 0

while start <= end:
    count = 0
    mid = (start + end) // 2

    for i in cables:
        count += i // mid

    if count < N:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid
print(answer)
