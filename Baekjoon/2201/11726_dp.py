# 1/4
# 11726 2xn 타일링

n = int(input())
dp = [0] * 1001
dp[0] = 1
dp[1] = 2

for i in range(2, n):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n-1] % 10007)
