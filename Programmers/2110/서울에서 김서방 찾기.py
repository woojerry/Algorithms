# 10/10

def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            position = i

    answer = '김서방은 ' + str(position) + "에 있다"
    return answer
