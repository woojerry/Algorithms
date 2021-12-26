# 12/26
# 18512 점프 점프

# 멀리 뛰는 거리, 시작점
X, Y, P1, P2 = map(int, input().split())

t_x, t_y = 0, 0
d_x, d_y = 0, 0
answer = -1
cnt = 0
while cnt < 100:
    cnt += 1
    if P1 == P2:
        print(P1)
        break
    d_x = P1 + t_x * X
    d_y = P2 + t_y * Y

    if d_x == d_y:
        answer = d_x
        break
    elif d_x > d_y:
        t_y += 1
    else:
        t_x += 1

print(answer)
