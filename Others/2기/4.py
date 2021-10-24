# max(x), min(x) 함수 안 x의 자료형은 iterable해야한다.
def check_page(pages):
    if pages[0] % 2 != 1:
        return False
    if pages[1] % 2 != 0:
        return False
    if pages[1] - pages[0] != 1:
        return False
    return True


def make_score(pages):
    score_list = []
    left_sum = 0
    left_mul = 1
    for i in str(pages[0]):
        left_sum += int(i)
        left_mul *= int(i)
    score_list.append(left_sum)
    score_list.append(left_mul)

    right_sum = 0
    right_mul = 1
    for i in str(pages[1]):
        right_sum += int(i)
        right_mul *= int(i)
    score_list.append(right_sum)
    score_list.append(right_mul)

    return max(score_list)


def solution(pobi, crong):
    if check_page(pobi) and check_page(crong):
        pobi_score = make_score(pobi)
        crong_score = make_score(crong)

        if pobi_score > crong_score:
            answer = 1
        elif pobi_score == crong_score:
            answer = 0
        else:
            answer = 2

    else:
        answer = -1

    return answer


print(solution([97, 98], [197, 198]))
print(solution([131, 132], [211, 212]))
print(solution([99, 102], [211, 212]))
