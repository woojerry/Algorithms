# 03/15
# 1913 달팽이
import sys
read = sys.stdin.readline

N = int(read())  # 홀수
target = int(read())

dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
graph = [[0] * N for _ in range(N)]
num = N*N

r, c = 0, 0
graph[r][c] = num

pivot = N-1
dir = 0
while pivot > 0:
    for _ in range(pivot):
        nr, nc = r + dirs[dir][0], c + dirs[dir][1]

        if graph[nr][nc] != 0:
            pivot -= 1
            break

        else:
            r, c = nr, nc
            num -= 1
            graph[r][c] = num
    dir = (dir + 1) % 4

print(dir, pivot, num)

for i in range(N):
    for j in range(N):
        print(graph[i][j], end=' ')
        if graph[i][j] == target:
            ans_r, ans_c = i, j
    print()

print(ans_r, ans_c)
