
# num 계속 증가시키고
# direction을 계속바꾸고, 한대각선당 개수

# dir = [left_down, right_up]
# left_down이면 r,c를 (1,-1) 경계에 닿으면 row만 +1 (1,0)
# right_up이면 r,c를 (-1,1) 경계에 닿으면 column +1

N = int(input())
dr = [1, -1]  # left down
dc = [-1, 1]  # right up


dir = 0
r, c = 0, 0
#nr, nc = 0, 0
graph = [[0] * N for _ in range(N)]
num = 1

while True:
    if num > (N*N):
        break
    graph[r][c] = num
    if dir == 0:  # left down
        nr = r + dr[0]
        nc = c + dc[0]
        if nc < 0:
            nr = r + 1
            nc = c
            dir = 1
        if nr >= N:
            nr = r
            nc = c + 1
            dir = 1
    elif dir == 1:  # right up
        nr = r + dr[1]
        nc = c + dc[1]
        if nr < 0:
            nr = r
            nc = c + 1
            dir = 0
        if nc >= N:
            nr = r + 1
            nc = c
            dir = 0

    r, c = nr, nc
    num += 1

for i in range(N):
    print("")
    for j in range(N):
        print(graph[i][j], end=" ")
