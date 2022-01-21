# 01/21
# 1837 암호제작
# 에라토스테네스의 체
import sys
read = sys.stdin.readline

P, K = map(int, read().split())
K -= 1

is_prime = [False, False] + [True] * (K-1)
primes = []
for i in range(2, K+1):
    if is_prime[i]:
        primes.append(i)
        for j in range(2*i, K+1, i):  # 2부터 시작해서 특정 수의 배수에 해당하는 수를 모두 판별
            is_prime[j] = False


answer = 'GOOD'
for prime in primes:
    if P % prime == 0:
        answer = (f'BAD {prime}')
        break

print(answer)
