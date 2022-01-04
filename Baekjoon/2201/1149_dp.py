# 1/4
# 1149 RGB거리

N = int(input())
dp = []
for _ in range(N):
    dp.append(list(map(int, input().split())))

for i in range(1, N):  # i번째 집을 각각의 색으로 칠했을 때의 최솟값
    # R
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0]
    # G
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + dp[i][1]
    # B
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + dp[i][2]

print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))

print(dp)
