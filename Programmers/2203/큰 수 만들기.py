def solution(number, k):
    stack = []

    count = 0
    for num in number:
        while count < k and stack and stack[-1] < num:
            stack.pop()
            count += 1

        stack.append(num)

    while count < k:
        stack.pop()
        count += 1

    return ''.join(stack)


print(solution("1924", 2))
