# 1/4
# 9095 1,2,3 더하기

T = int(input())
dp = [1, 2, 4]
for i in range(3, 10):
    dp.append(dp[i-3] + dp[i-2] + dp[i-1])

for _ in range(T):
    n = int(input())
    print(dp[n-1])
