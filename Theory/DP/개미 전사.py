# 개미 전사를 위한 식량창고 N개에 대한 정보가 주어졌을 때 얻을 수 있는 식량의 최댓값?
# 인접한 식량창고 접근 X, 최소한 한 칸 이상 떨어진 식량창고를 약탈해야 함
# 3 <= N <= 100
# 둘째 줄에 공백을 기준으로 각 식량창고에 저장된 식량의 개수 K가 주어짐

# 4
# 1 3 1 5
# 답 8

N = int(input())
storage = list(map(int, input().split()))
d = [0] * 100
d[0] = storage[0]
d[1] = max(storage[0], storage[1])
for i in range(2, N):
    d[i] = max(d[i - 1], d[i-2] + storage[i])

print(d[N-1])
