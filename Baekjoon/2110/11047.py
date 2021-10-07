# 10/06
# 11047 동전0

N, K = map(int, input().split())
coin = []

for i in range(N):
    coin.append(int(input()))

coin.reverse()

result = 0

for i in coin:
    if(K // i) > 0:
        result += (K // i)
        K %= i

print(result)
