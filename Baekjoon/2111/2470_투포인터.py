# 11/24
# 2470 두 용액

import sys

read = sys.stdin.readline
N = int(read())  # 용액의 수

solutions = sorted(list(map(int, read().rstrip().split())))

left, right = 0, N-1
minimum = ''
answer = []

while left < right:
    total = solutions[left] + solutions[right]
    if minimum == '':
        minimum = abs(total)
        answer = [solutions[left], solutions[right]]
    elif minimum > abs(total):
        minimum = abs(total)
        answer = [solutions[left], solutions[right]]

    if total < 0:
        left += 1
    elif total > 0:
        right -= 1
    else:
        break

print(answer[0], answer[1])
