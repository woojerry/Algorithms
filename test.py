import heapq

INF = int(1e9)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    a, b = map(int, input().split())

    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    q = []
    # (dist, now)
    distance = [[INF, -1]] * (n + 1)
    distance[a] = [0, a]
    distance[b] = [0, b]

    cand_a = []
    cand_b = []
    cand_n = []

    # tuple(dist, now, start)
    heapq.heappush(q, (0, a, a))
    heapq.heappush(q, (0, b, b))

    neutral = []

    while q:
        dist, now, start = heapq.heappop(q)
        if distance[now][0] < dist:
            continue

        for next in graph[now]:
            cost = dist + 1

            if cost == distance[next][0] and start != distance[next][1]:
                heapq.heappush(neutral, (cost, next))

            if cost < distance[next][0]:
                distance[next] = [cost, start]
                heapq.heappush(q, (cost, next, start))

                if start == a:
                    cand_a.append(next)
                else:
                    cand_b.append(next)

    if neutral:
        for i in range(1, len(distance)):
            if distance[i][0] >= neutral[0][0]:
                if i in cand_a:
                    cand_a.remove(i)
                    cand_n.append(i)
                elif i in cand_b:
                    cand_b.remove(i)
                    cand_n.append(i)

        for d, n in distance:
            if d >= neutral[0][0]:
                if n in cand_a:
                    cand_a.remove(n)
                    cand_n.append(n)
                elif n in cand_b:
                    cand_b.remove(n)
                    cand_n.append(n)
    print(cand_a)
    print(cand_b)
    print(cand_n)
