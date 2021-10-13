# 10/13
# 1018 체스판 다시 칠하기

N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

array = []


for x in range(N - 7):
    for y in range(M - 7):

        paint_W = 0
        paint_B = 0
        for i in range(x, x+8):
            for j in range(y, y+8):
                if(i+j) % 2 == 0:  # 짝수
                    if board[i][j] != 'W':
                        paint_W += 1
                    if board[i][j] != 'B':
                        paint_B += 1
                else:  # 홀수
                    if board[i][j] != 'B':
                        paint_W += 1
                    if board[i][j] != 'W':
                        paint_B += 1

        array.append(min(paint_W, paint_B))


print(min(array))
