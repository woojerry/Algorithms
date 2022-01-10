# 1/10
# 4811 알약

while True:
    N = int(input())  # N <= 31
    if N == 0:
        break

    dp = [[0] * (N+1) for _ in range(N+1)]

    for i in range(N+1):  # 반개를 0번 먹었을 때
        dp[0][i] = 1

    for i in range(1, N+1):
        for j in range(i, N+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    print(dp[N][N])
