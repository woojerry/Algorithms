# 09/28
# 10250 ACM호텔

T = int(input())

for _ in range(T):
    room = []
    H, W, N = map(int, input().split())

    for j in range(1, W+1):
        for i in range(1, H+1):
            if j > 9:
                room.append(str(i)+str(j))
            else:
                room.append(str(i)+'0'+str(j))
    print(int(room[N-1]))
