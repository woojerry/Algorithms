# 10/14

def solution(answers):
    score = [0, 0, 0]
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = []

    for i in range(len(answers)):  # 반복되는 배열들에 대한 처리
        if one[i % 5] == answers[i]:
            score[0] += 1
        if two[i % 8] == answers[i]:
            score[1] += 1
        if three[i % 10] == answers[i]:
            score[2] += 1
    max_score = max(score)

    for i in range(3):
        if score[i] == max_score:
            answer.append(i+1)

    return answer


print(solution([1, 2, 3, 4, 5]))
