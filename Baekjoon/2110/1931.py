# 10/15
# 1931 회의실 배정

N = int(input())  # 회의의 수
times = []

# times = [tuple(map(int, input.split())) for _ in range(N)]
for _ in range(N):
    start, end = map(int, input().split())
    times.append((start, end))

times.sort(key=lambda x: (x[1], x[0]))

end_time = times[0][1]
answer = 1
for i in range(1, len(times)):
    if times[i][0] >= end_time:
        answer += 1
        end_time = times[i][1]

print(answer)
