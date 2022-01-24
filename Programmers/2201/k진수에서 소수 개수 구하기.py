def convert_notation(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)

    return convert_notation(q, base) + T[r] if q else T[r]


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0

    if k != 10:
        converted = convert_notation(n, k)
    else:
        converted = str(n)

    cands = list(converted.split('0'))

    for cand in cands:
        if cand == '':
            continue
        else:
            if is_prime(int(cand)):
                answer += 1

    return answer


#print(solution(437674, 3))
print(solution(110011, 10))
