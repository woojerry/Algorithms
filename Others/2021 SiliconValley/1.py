def solution(rows, columns, connections, queries):
    # graph = [[[] for _ in range(columns)] for _ in range(rows)]
    # for i in connections:  # 초기 그래프
    #     a, b, c, d = i[0]-1, i[1]-1, i[2]-1, i[3]-1
    #     graph[a][b].append((c, d))
    #     graph[c][d].append((a, b))
    answer = []
    out_range = []
    for query in queries:
        origin_connections = len(connections)
        r1, c1, r2, c2 = query[0], query[1], query[2], query[3]
        if r1 > r2:  # r1을 더 작게끔
            r1, r2 = r2, r1
        if c1 > c2:  # c1을 더 작게끔
            c1, c2 = c2, c1

        if r1 != 1:  # 윗변
            for col in range(c1, c2+1):
                out_range.append([r1-1, col, r1, col])
                out_range.append([r1, col, r1-1, col])
        if r2 != rows:  # 아랫변
            for col in range(c1, c2+1):
                out_range.append([r2, col, r2+1, col])
                out_range.append([r2+1, col, r2, col])
        if c1 != 1:  # 왼쪽변
            for row in range(r1, r2+1):
                out_range.append([row, c1-1, row, c1])
                out_range.append([row, c1, row, c1 - 1])
        if c2 != columns:  # 오른쪽변
            for row in range(r1, r2+1):
                out_range.append([row, c2, row, c2+1])
                out_range.append([row, c2+1, row, c2])

        for out in out_range:
            if out in connections:
                connections.remove(out)

        answer.append(origin_connections - len(connections))

    return answer


print(solution(4, 3, [[1, 1, 2, 1], [1, 2, 1, 3], [1, 3, 2, 3], [2, 2, 2, 3], [2, 2, 3, 2], [
      2, 3, 3, 3], [3, 2, 3, 3], [3, 2, 4, 2], [4, 1, 4, 2]], [[2, 2, 3, 1], [1, 2, 4, 2]]))

print(solution(2, 2, [[1, 1, 1, 2], [2, 2, 1, 2], [2, 1, 1, 1], [
      2, 2, 2, 1]], [[1, 1, 2, 2], [1, 1, 2, 1], [2, 1, 2, 2]]))

print(solution(3, 3, [[1, 1, 2, 1], [2, 1, 3, 1], [1, 2, 2, 2], [2, 2, 3, 2], [
      1, 3, 2, 3], [2, 3, 3, 3]], [[1, 1, 3, 1], [1, 2, 3, 2], [1, 3, 3, 3]]))
