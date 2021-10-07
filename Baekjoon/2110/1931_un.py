# 10/06
# 1931 회의실 배정

N = int(input())  # 회의의 수
times = []

# times = [tuple(map(int, input.split())) for _ in rang(N)]
for _ in range(N):
    start, end = map(int, input().split())
    times.append((start, end))


print(times)
