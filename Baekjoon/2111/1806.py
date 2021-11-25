# 11/25
# 1806 부분합

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

total, start, end = 0, 0, 0
min_length = 100000

for start in range(N):
    while total < S and end < N:
        total += numbers[end]
        end += 1
    if total >= S:
        min_length = min(min_length, end - start)
    total -= numbers[start]

if min_length == 100000:
    min_length = 0
print(min_length)
