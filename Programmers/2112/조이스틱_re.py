# 12/06

def solution(name):
    answer = 0
    up_down = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11,
               "M": 12, "N": 13, "O": 12, "P": 11, "Q": 10, "R": 9, "S": 8, "T": 7, "U": 6, "V": 5, "W": 4, "X": 3, "Y": 2, "Z": 1}

    visited = [1] * (len(name))
    for i in range(len(name)):  # 가중치 더하기
        answer += up_down[name[i]]
        if name[i] == 'A':
            visited[i] = 0
    cursor = 0

    while True:
        visited[cursor] = 0
        if sum(visited) == 0:
            return answer

        left, right = 1, 1
        while visited[cursor - left] == 0:
            left += 1
        while visited[cursor + right] == 0:
            right += 1
        if left < right:  # python은 음수면 역으로
            answer += left
            cursor -= left
        else:
            answer += right
            cursor += right


print(solution('ZAAAZZZZZZZ'))  # 15
# print(solution('JAZ'))
# print(solution("JEROEN"))
# print(solution("JAN"))
