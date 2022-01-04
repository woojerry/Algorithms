# N개 종류의 화폐, 갯수는 무제한
# M원을 만들기 위한 최소한의 화폐 개수
# 1<
N, M = map(int, input().split())
units = list(int(input()) for _ in range(N))

dp = [10001] * (M+1)
dp[0] = 0
for i in range(N):  # 각각의 화폐 단위에 대해
    for j in range(units[i], M+1):
        if dp[j - units[i]] != 10001:  # (i-k)원을 만드는 방법이 존재하는 경우
            dp[j] = min(dp[j], dp[j-units[i]] + 1)

if dp[M] == 10001:  # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(dp[M])
