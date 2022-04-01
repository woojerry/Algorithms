# 04/01
# 15810 풍선공장
import sys
read = sys.stdin.readline

N, M = map(int, read().split())  # 스태프, 풍선
balloon_times = sorted(list(map(int, read().split())))

start, end = 1, balloon_times[-1] * M
while start <= end:
    mid = (start + end) // 2

    count = 0
    for time in balloon_times:
        count += mid // time
        if count >= M:
            break

    if count >= M:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
