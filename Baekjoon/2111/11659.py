# 11/19
# 11659 구간 합 구하기 4

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numbers = list(map(int, input().split()))
sum_list = [0]
total = 0
for i in range(len(numbers)):
    total += numbers[i]
    sum_list.append(total)

for _ in range(M):
    start, end = map(int, input().split())
    print(sum_list[end] - sum_list[start-1])
