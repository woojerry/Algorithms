# 10/18
# 5911 선물

N, B = map(int, input().split())
list = []

for _ in range(N):
    a, b = map(int, (input().split()))
    list.append([a, b])

list.sort(key=lambda x: (x[0] + x[1], x[1]))

answer = []

for i in range(N):
    money = B
    if i != 0:
        list[i-1][0] *= 2

    list[i][0] //= 2
    cnt = 0

    for j in range(0, len(list)):
        money -= (list[j][0] + list[j][1])
        if money >= 0:
            cnt += 1

    answer.append(cnt)

print(max(answer))
