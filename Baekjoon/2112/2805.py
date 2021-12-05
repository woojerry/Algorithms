# 12/03
# 2805 나무 자르기
import sys

read = sys.stdin.readline
N, M = map(int, read().rstrip().split())
trees = list(map(int, read().rstrip().split()))
start, end = 0, max(trees)
answer = 0

while start <= end:
    woods = 0
    mid = (start + end) // 2  # 0과 최대의 중간값

    woods = sum([i - mid if mid < i else 0 for i in trees])  # sum이 시간덜걸림

    if woods < M:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)
