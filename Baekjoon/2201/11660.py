# 01/26
# 11660 구간 합 구하기5
# 누적합, DP
import sys
read = sys.stdin.readline

N, M = map(int, read().split())
dp = [[0] * (N+1) for _ in range(N+1)]
graph = [list(map(int, read().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i + 1]
                            [j] - dp[i][j]) + graph[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, read().split())

    print(dp[x2][y2] - (dp[x1 - 1][y2] + dp[x2][y1 - 1] - dp[x1 - 1][y1 - 1]))
