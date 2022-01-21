# 01/18
# 1072 게임

X, Y = map(int, input().split())

start, end = 0, X
answer = 0

Z = Y * 100 // X

if Z >= 99:
    print(-1)

else:
    while start <= end:
        mid = (start + end) // 2

        changed_rate = (Y + mid) * 100 // (X+mid)
        if changed_rate > Z:
            answer = mid
            end = mid - 1

        else:
            start = mid + 1

    print(answer)
