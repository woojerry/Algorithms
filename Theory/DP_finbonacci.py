# 피보나치 수열 Top-down DP
# 시간복잡도 O(N)
d = [0] * 100


def fibo(x):
    # 종료 조건 (1 혹은 2일 때 1을 반환)
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)

    return d[x]


print(fibo(99))
