# n x m 크기의 금광
# 맨 처음에은 첫 번째 열의 어느 행에서든 출발할 수 있다.
# 이후 m-1번에 걸쳐 매번 오른쪽 위, 오른쪽, 오른쪽 아래로 이동해야한다. 채굴자가 얻을 수 있는 금의 최대 크기를 구하시오

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m

    # DP
    for j in range(1, m):  # 열을 오른쪽으로 가면서
        for i in range(n):  # 열마다 전체 행 확인
            # 왼쪽 위
            if i == 0:  # 범위 밖인지
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            # 왼쪽 아래
            if i == n-1:  # 범위 밖인지
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            # 왼쪽에서 오는 경우
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    result = 0
    for i in range(n):  # 가장 오른쪽 열에 있는 값중 제일 큰값이 answer
        result = max(result, dp[i][m-1])
    print(result)
