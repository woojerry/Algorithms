# 12/7
# 21318 피아노 체조
# 누적합

import sys
read = sys.stdin.readline

N = int(read())
levels = list(map(int, read().split()))
mistakes, cnt = [], 0
for i in range(0, N):
    if i == 0:
        mistakes.append(cnt)
        continue
    else:
        if levels[i-1] > levels[i]:
            cnt += 1
    mistakes.append(cnt)

Q = int(read())

for _ in range(Q):
    x, y = map(int, read().split())
    print(mistakes[y-1] - mistakes[x-1])
