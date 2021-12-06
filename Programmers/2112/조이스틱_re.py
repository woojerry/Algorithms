def solution(name):
    answer = 0
    up_down = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11,
               "M": 12, "N": 13, "O": 12, "P": 11, "Q": 10, "R": 9, "S": 8, "T": 7, "U": 6, "V": 5, "W": 4, "X": 3, "Y": 2, "Z": 1}

    visited = [1] * (len(name)-1)
    visited[0] = 0
    for i in range(len(name)):  # 가중치 더하기
        answer += up_down[name[i]]
        if name[i] == 'A':
            visited[i] = 0

    cursor = 0

    # for j in range(len(name)):  # 이동거리 더하기
    while sum(visited) != 0:
        left, right = cursor, cursor
        left_cnt, right_cnt = 0, 0

        while name[right] != 'A':
            right += 1
            right_cnt += 1
            if right == len(name)-1:
                right = 0
        while name[left] != 'A':
            left -= 1
            left_cnt += 1
            if left == -1:
                left = len(name) - 1
        if left_cnt >= right_cnt:
            cursor = right
            answer += right_cnt
        else:
            cursor = left
            answer += left_cnt
        visited[cursor] = 0
        # if name[j] == 'A':
        #     continue
        # else:
        #     right = abs(j - cursor)
        #     left = abs(cursor + len(name) - j)
        #     #print(right, left)
        #     if right >= left:
        #         answer += left
        #     else:
        #         answer += right
        #     cursor = j
        # print(name[j], answer)

    return answer


print(solution('ZAAAZZZZZZZ'))  # 15
# print(solution('JAZ'))
# print(solution("JEROEN"))
# print(solution("JAN"))
