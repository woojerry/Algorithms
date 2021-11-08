def solution(s):
    answer = []

    cont = 1
    tmp = ''
    for i in range(len(s)):
        print(answer)
        if i == 0:  # 처음
            first = s[i]
            tmp = s[i]

        elif i == (len(s) - 1):  # 마지막

            if s[i] == tmp:
                cont += 1
            else:
                answer.append(cont)
            answer.append(cont)

            last = s[i]
            if first == last:
                # print(answer)
                answer[0] += answer[-1]
                length = len(answer)
                answer = answer[0: (length-1)]

        else:
            if s[i] == tmp:  # 연속됐을 때
                cont += 1

            else:
                tmp = s[i]
                answer.append(cont)
                cont = 1
                # print(last)
                # print(i)
                #print(len(s) - 1)

    return sorted(answer)


# print(solution("aaabbaaa"))
print(solution("wowwow"))
