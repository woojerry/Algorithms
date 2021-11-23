# 11/23
# 3273 두 수의 합
import sys

read = sys.stdin.readline

n = int(read())
numbers = sorted(list(map(int, read().rstrip().split())))  # 정렬
x = int(read())
end, count = n-1, 0

for start in range(n):
    while start < end:
        if numbers[start] + numbers[end] == x:
            count += 1
            break
        elif numbers[start] + numbers[end] < x:
            break
        else:
            end -= 1
print(count)
