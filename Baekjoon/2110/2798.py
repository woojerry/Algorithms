# 10/12
# 2798 블랙잭

N, M = map(int, input().split())
cards = list(map(int, input().split()))
answer = []

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum = cards[i] + cards[j] + cards[k]
            if sum <= M:
                answer.append(sum)

print(max(answer))
