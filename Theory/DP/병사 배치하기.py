# N명의 병사가 무작위로 나열돼있을 때
# 전투력이 높은 병사가 앞쪽으로 오도록 내림차순으로
# 특정한 위치에 있는 병사를 열외시켜 내림차순 만들기

# 가장 긴 증가하는 부분 수열 LIS 아이디어 사용
# 이문제 에서는 내림차순 이므로 반대로

N = int(input())  # 1<= N <= 2000
array = list(map(int, input().split()))
# 순서를 뒤집어 내림차순 -> 최장 증가 부분 수열로 변환
array.reverse()

# DP를 위한 1차원 DP테이블 초기화
dp = [1] * N

# LIS 알고리즘 수행
for i in range(1, N):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 열외해야 하는 병사의 최소 수를 출력
print(N-max(dp))
