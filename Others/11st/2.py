# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    pass

    blocks = []

    tmp = ''
    num = 0
    for i in range(len(S)):
        if i == 0:
            tmp = S[i]
            num = 1

        elif tmp == S[i]:
            num += 1

            if i == len(S) - 1:
                blocks.append(num)

        elif tmp != S[i]:
            blocks.append(num)
            num = 1
            tmp = S[i]

            if i == len(S) - 1:
                blocks.append(num)

    max_block = max(blocks)

    answer = 0
    for j in blocks:
        if j < max_block:
            answer += max_block - j

    return answer


print(solution("bbbab"))
