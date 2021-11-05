# 11/03
from collections import deque


def bfs(room):
    people = []
    for i in range(5):
        for j in range(5):
            if room[i][j] == "P":
                people.append((i, j))

    queue = deque(people)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        r, c = queue.popleft()
        for q in range(4):
            nr = r + dr[q]
            nc = c + dc[q]

            if 0 <= nr < 5 and 0 <= nc < 5:
                if room[nr][nc] == 'P':
                    return 0

                elif room[nr][nc] == 'O':
                    for p in range(4):
                        nr = nr + dr[p]
                        nc = nc + dc[p]
                        if 0 <= nr < 5 and 0 <= nc < 5:
                            if nr == r and nc == c:
                                continue

                            if room[nr][nc] == 'P':
                                return 0
    return 1


def solution(places):
    answer = []

    for k in range(5):
        answer.append(bfs(places[k]))

    return answer
