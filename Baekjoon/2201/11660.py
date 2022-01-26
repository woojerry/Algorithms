# 01/26
# 11660 구간 합 구하기5
# 누적합, DP

N, M = map(int, input().split())
dp = [[0] * N for _ in range(N+1)]
graph = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = graph[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

for _ in range(M):
    x1, x2, y1, y2 = map(int, input().split())


# print(numbers[x2][y2] - numbers[x1 - 1][y2] - numbers[x2][y1 - 1] + numbers[x1 - 1][y1 - 1])
    answer = dp[x2][y2] - dp[x2 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]
    print(answer)
