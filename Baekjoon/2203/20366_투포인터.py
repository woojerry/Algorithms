# 03/08
# 20366 같이 눈사람 만들래?
# 투 포인터
# 4포인터 중 2개 고정 후 2포인터

import sys
read = sys.stdin.readline

N = int(read())  # N <= 600, N^3 + two pointer
snowballs = sorted(list(map(int, read().split())))

diff = 1000000000
for i in range(N-3):
    for j in range(i+3, N):
        pivot_snowman = snowballs[i] + snowballs[j]
        start, end = i+1, j-1

        while start < end:
            new_snowman = snowballs[start] + snowballs[end]

            diff = min(diff, abs(pivot_snowman - new_snowman))

            if pivot_snowman > new_snowman:
                start += 1
            elif pivot_snowman < new_snowman:
                end -= 1
            else:
                print(0)
                exit()

print(diff)
