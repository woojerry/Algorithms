# 10/07
# 13305 주유소

N = int(input())  # 도시의 개수

distance = list(map(int, input().split()))
price = list(map(int, input().split()))

opt_price = price[0]  # 최적의 기름값
total_price = 0

total_price += opt_price * distance[0]  # 처음거리 비용

for i in range(1, N-1):
    if opt_price > price[i]:
        opt_price = price[i]
    total_price += opt_price * distance[i]

print(total_price)
