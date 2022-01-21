# 2부터 n까지의 소수 찾기위해 n 입력
n = int(input())
# 1은 소수가 아니고 인덱스가 수를 의미하기 위해 원소는 n + 1개
is_prime = [False, False] + [True] * (n - 1)
primes = []  # 소수 모음

for i in range(2, int(n ** 0.5) + 1):   # 2부터 n의 제곱근까지
    if is_prime[i]:  # i가 소수이면(True) 소수 모음에 추가
        primes.append(i)
        for j in range(2 * i, n + 1, i):  # i를 제외한 2 * i부터 모든 배수 지움
            is_prime[j] = False

print(primes)
