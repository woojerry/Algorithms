# 03/14
# 12865 평범한 배낭
# DP

import sys
read = sys.stdin.readline

N, K = map(int, read().split())

# 0번째 인덱스를 위한 빈값도 넣어주기
weights, values = [[]], [[]]

for _ in range(N):
    W, V = map(int, read().split())
    weights.append(W)
    values.append(V)

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(0, K+1):
        if j < weights[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(values[i] + dp[i-1][j - weights[i]], dp[i-1][j])

print(dp[N][K])
