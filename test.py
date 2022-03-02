N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

answer = 0
coins.sort(reverse=True)
for i in range(N):
    print(K, coins[i])
    if K % coins[i] != K:
        answer += K // coins[i]
        K = K % coins[i]
        
print(answer)