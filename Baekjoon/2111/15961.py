import sys

read = sys.stdin.readline

N, d, k, c = map(int, read().rstrip().split())
sushi = [int(read()) for _ in range(N)]

end, count, max_count = 0, 0, 0
choice = {c: 1}

for start in range(N):
    if end == N:  # 회전초밥이므로
        end = 0
    while count < k and end < N:
        su = sushi[end]
        choice[su] = choice.get(su, 0) + 1
        end += 1
        count += 1
    max_count = max(max_count, len(choice))
    if max_count == k + 1:
        break
    su_st = sushi[start]
    count -= 1
    if choice[su_st] > 1:
        choice[su_st] -= 1
    else:
        choice.pop(su_st)

print(max_count)
