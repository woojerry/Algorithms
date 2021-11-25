# 11/24
# 2003 수들의 합2

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

right = 0
total = 0
count = 0

for left in range(N):
    while total < M and right < N:
        total += numbers[right]
        right += 1
    if total == M:
        count += 1
    total -= numbers[left]

print(count)
