# 03/08
# 21608 상어 초등학교
# 구현 + bfs + 브루트포스

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N = int(input())
classroom = [[0] * N for _ in range(N)]
dic = {}
score = [0, 1, 10, 100, 1000]

for n in range(N*N):
    tmp = list(map(int, input().split()))

    student, favor = tmp[0], tmp[1:]
    dic[student] = favor
    max_like, max_empty = -1, -1
    cand = (N+1, N+1)
    for r in range(N):
        for c in range(N):
            if classroom[r][c] == 0:  # 비어있는 칸
                favor_count = 0
                empty_count = 0

                for q in range(4):
                    nr = r + dr[q]
                    nc = c + dc[q]

                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        continue

                    if classroom[nr][nc] in favor:
                        favor_count += 1

                    if classroom[nr][nc] == 0:
                        empty_count += 1

                if favor_count > max_like:
                    cand = (r, c)
                    max_like = favor_count
                    max_empty = empty_count

                elif favor_count == max_like:
                    if empty_count > max_empty:
                        cand = (r, c)
                        max_empty = empty_count
                    elif empty_count == max_empty:
                        recent_r, recent_c = cand
                        if recent_r > r:
                            cand = (r, c)
                        elif recent_r == r:
                            if recent_c > c:
                                cand = (r, c)

    pos_r, pos_c = cand
    classroom[pos_r][pos_c] = student

answer = 0
for r in range(N):
    for c in range(N):
        count = 0
        for q in range(4):
            nr = r + dr[q]
            nc = c + dc[q]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            if classroom[nr][nc] in dic[classroom[r][c]]:
                count += 1
        answer += score[count]

print(answer)
