# 1번 관계선 인접리스트로 저장하고 쿼리 마다 x,y 최대최소잡고 4변 따라 관계선 찾아보면서 최대최소 밖으로 나가는 관계선 있으면 다 짜르고 카운팅해서 답 배열에 어펜드
def make_rect(r1, c1, r2, c2):
    if r1 == r2:
        return [(r1, c1), (r1, c2)]
    # elif c1 == c2


def solution(rows, columns, connections, queries):
    answer = []
    graph = [[[] for _ in range(columns)] for _ in range(rows)]
    print(graph)

    for i in connections:  # 초기 그래프
        a, b, c, d = i[0]-1, i[1]-1, i[2]-1, i[3]-1
        graph[a][b].append((c, d))
        graph[c][d].append((a, b))
    print(graph[0])

    # for j in queries:
    #     r1, c1, r2, c2 = j[0]-1, j[1] - 1, j[2]-1, j[3] - 1
    #     if r1 == r2:
    #         if c2 >= c1:
    #         else:
    #     elif c1 == c2:
    #     else:
    #         for pos in graph[r1][c1]:
    #             if pos[0] < r1 or pos[1]

    return answer


print(solution(4, 3, [[1, 1, 2, 1], [1, 2, 1, 3], [1, 3, 2, 3], [2, 2, 2, 3], [2, 2, 3, 2], [
      2, 3, 3, 3], [3, 2, 3, 3], [3, 2, 4, 2], [4, 1, 4, 2]], [[2, 2, 3, 1], [1, 2, 4, 2]]))
