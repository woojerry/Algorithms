from collections import deque


def solution(rows, columns):
    answer = [[0] * columns for _ in range(rows)]
    visited = [[(rows, columns)] * columns for _ in range(rows)]

    queue = deque()
    queue.append((0, 0))
    num = 1
    answer[0][0] = 1
    zero = (rows * columns)
    zero -= 1
    while True:
        r, c = queue.popleft()

        if num % 2 == 0:  # 짝수
            nr = r + 1
            nc = c
            if nr == (rows):
                nr = 0
        else:  # 홀수
            nr = r
            nc = c+1
            if nc == (columns):
                nc = 0

        if zero < 1:
            break

        if visited[nr][nc] == (r, c):
            # 0,0관련 처리
            if (r, c) == (0, 0):  # 이전이 0,0에서 온거면 다시 바꿔주기?
                answer[0][0] = 1
            break

        if answer[nr][nc] == 0:
            zero -= 1

        num += 1
        answer[nr][nc] = num

        visited[nr][nc] = (r, c)  # 이전
        queue.append((nr, nc))

    return answer


#print(solution(3, 4))
print(solution(3, 3))
print(solution(3, 9))
print(solution(4, 8))
