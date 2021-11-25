def solution(input_str, k):
    answer = ''
    for start in range(len(input_str)):
        end = start
        tmp = ''
        count = 0

        while end < len(input_str):
            if input_str[end] == '1':
                count += 1
            tmp += input_str[end]

            if count == k:
                if answer == '':
                    answer = tmp
                else:
                    if len(tmp) < len(answer):  # 길이가 짧은 것
                        answer = tmp
                    elif len(tmp) == len(answer):  # 사전순
                        if tmp < answer:
                            answer = tmp
                break
            end += 1

    return answer


print(solution("0101101", 3))  # 1011
print(solution("10101", 2))  # 101
print(solution("110011101", 4))  # 11101
