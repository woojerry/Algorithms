# 11/16

def solution(s):
    length = []
    result = ''

    if len(s) == 1:
        return 1

    for i in range(1, (len(s) // 2 + 1)):
        tmp = s[:i]
        num = 1  # 앞의 번호
        for j in range(i, len(s), i):
            if s[j:j+i] == tmp:  # 동일한 문자일 경우 앞의 숫자 올려줌
                num += 1
            else:
                if num == 1:
                    num = ''
                result += str(num) + tmp
                tmp = s[j:i+j]
                num = 1

        if num == 1:
            num = ''
        result += str(num) + tmp
        length.append(len(result))
        result = ''

    return min(length)


print(solution("aabbaccc"))
