# 10/26
# 다리 놓기

T = int(input())
for i in range(T):
    N, M = map(int, input().split())

    answer = 1  # 조합 그대로의 공식으로
    for a in range(1, M+1):
        answer *= a
    for b in range(1, N+1):
        answer //= b
    for c in range(1, M-N+1):
        answer //= c

    print(answer)
