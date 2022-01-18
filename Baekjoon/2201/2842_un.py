# 01/18
# 2842 집배원 한상덕

N = int(input())
graph, altitude = [], []
houses = []

# 우체국은 'P', 집은 'K', 목초지는 '.'
for i in range(N):
    graph.append(list(input()))
    for j in range(N):
        if graph[i][j] == 'P':
            sangduck = (i, j)
        elif graph[i][j] == 'K':
            houses.append((i, j))

for _ in range(N):
    altitude.append(list(map(int, input().split())))

dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]
