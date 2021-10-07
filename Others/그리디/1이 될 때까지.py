# 어떠한 수 N이 1이 될 때까지 다음 두 과정 중 하나를 반복해서 수행한다. 두 과정은 아래와 같다.

# N에서 1을 뺀다.
# N을 K로 나눈다. (단, 나눌 수 있는 경우만 해당된다.)
# 예를 들어서 N이 17이고, K가 4라면 처음에는 나눌 수 없으므로 1을 뺀다. 그뒤 16이 되면 K값 4로 나눌 수 있기 때문에 나누어준다. 그러면 4가 되는데 또 K값으로 나눠줄 수 있기 때문에 나눠주면 1 이므로 종료된다.

# 이때 결과는 총 3번 과정을 수행했으므로 3을 출력하면된다.

n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break
    # k로 나누기
    result += 1
    n //= k
result += (n-1)
print(result)


# 다른 풀이
n, k = map(int, input().split())

result = 0

while (n != 1):
    if n % k != 0:
        n -= 1
        result += 1
    else:
        n //= k
        result += 1

print(result)
