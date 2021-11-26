from itertools import combinations

N, M = map(int, input().split())

graph = []
home = []
chicken = []
# 치킨 거리를 갖고 있는 매장의 수 기준 ..?
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] == 1:
            home.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

comb_chicken = list(combinations(chicken, M))


answer = []

for combs in comb_chicken:
    chick_distance_total = 0
    for i in home:
        chick_distance = 0
        for j in combs:
            if chick_distance == 0:
                chick_distance = abs(
                    i[0] - j[0]) + abs(i[1] - j[1])
            else:
                chick_distance = min(chick_distance, abs(
                    i[0] - j[0]) + abs(i[1] - j[1]))
        chick_distance_total += chick_distance
    answer.append(chick_distance_total)

print(min(answer))
