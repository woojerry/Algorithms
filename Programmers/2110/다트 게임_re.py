# 10/17
def solution(dartResult):
    answer = 0

    score_opt = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 't']
    dartResult = dartResult.replace('10', 't')

    num = 0
    score = []

    for i in dartResult:
        if i in score_opt:
            if i == 't':
                num = 10
            else:
                num = int(i)
        if i == 'S':
            score.append(num)
            num = 0
        elif i == 'D':
            score.append(num * num)
            num = 0
        elif i == 'T':
            score.append(num*num*num)
            num = 0
        if i == '*':
            if(len(score) > 1):
                score[-1] *= 2
                score[-2] *= 2
            else:
                score[-1] *= 2
        elif i == '#':
            score[-1] *= -1

    answer = sum(score)

    return answer


print(solution('1S2D*3T'))
