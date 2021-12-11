# 12/11
# 11170 0의 개수
import sys
read = sys.stdin.readline
T = int(read())

for _ in range(T):
    N, M = map(int, read().split())
    count = 0
    for num in range(N, M+1):
        for i in str(num):
            if i == '0':
                count += 1
    print(count)
