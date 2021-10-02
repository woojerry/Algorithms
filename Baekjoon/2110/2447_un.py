# 10/01
# 2447 별 찍기 -10


N = int(input())

array = [[' ' for _ in range(N)] for _ in range(N)]

power = 0  # 몇 승인지
while N != 1:
    N = N / 3
    power += 1


# for i in range(N):
#     for j in range(N):
#         if(i % 3 == 1 and j % 3 == 1):
#             array[i][j] = " "
#         # if(i // 3) % 3 == 1 and (j // 3) % 3 == 1:
#         #     array[i][j] = " "


# def test(N):
#     if n < 3:
#         return
#     if(N == 3):
#         array[1][1] = " "
#     else:
#         cnt = int(N/3)  # 공백

#         for i in range(cnt):
#             for j in range(cnt):
#                 array[i+cnt][j+cnt] = " "

for _ in array:
    print("".join(_))
