
def solution(rows, columns, connections, queries):
    answer = []

    #graph = [ [0, 7 ,5], [7, 0 , INF], [5, INF, 0] ]

    graph = [[[] for _ in range(columns)] for _ in range(rows)]
    #graph = [[]]
    print(graph)
    # graph[0][0].append((1, 1))
    # print(graph)

    for i in connections:
        a, b, c, d = i[0]-1, i[1]-1, i[2]-1, i[3]-1
        # graph[a][b] = (c, d)
        graph[a][b].append((c, d))
        graph[c][d].append((a, b))
    # first, second = (i[0], i[1]), (i[2], i[3])
    # print(first, second)
    # graph[first[0][first[1]]] = second

    print(graph)

    return answer


print(solution(4, 3, [[1, 1, 2, 1], [1, 2, 1, 3], [1, 3, 2, 3], [2, 2, 2, 3], [2, 2, 3, 2], [
      2, 3, 3, 3], [3, 2, 3, 3], [3, 2, 4, 2], [4, 1, 4, 2]], [[2, 2, 3, 1], [1, 2, 4, 2]]))
