# 10/10

def solution(lottos, win_nums):
    correct = 0
    zero = 0
    for i in lottos:
        if i in win_nums:
            correct += 1
        if i == 0:
            zero += 1

    if correct + zero == 0:
        best = 6
        worst = 6
    elif correct == 0 and zero != 0:
        best = 7 - zero
        worst = 6
    else:
        best = 7 - (correct + zero)
        worst = 7 - correct

    return best, worst
