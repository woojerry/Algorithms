# 문자열 + 구현
def solution(expression):
    answer = 0

    # 숫자와 연산자 분리
    operators = ['*', '+', '-']
    get_operator = expression
    get_operator = get_operator.replace('*', ' ')
    get_operator = get_operator.replace('+', ' ')
    get_operator = get_operator.replace('-', ' ')
    nums = list(map(int, get_operator.split(' ')))
    real_operators = []
    for i in expression:
        if i in operators:
            real_operators.append(i)

    # 우선순위에 따라 계산
    priorities = ['*+-', '*-+', '+*-', '+-*', '-+*', '-*+']
    for priority in priorities:
        # 숫자들 우선순위 연산자마다 새롭게 초기화
        cur_nums = nums[:]
        cur_op = real_operators[:]

        for op in priority:
            nums_stack = []
            op_stack = []
            nums_stack.append(cur_nums[0])  # 숫자가 연산자보다 1개 많으므로 처음에 저장

            for j in range(len(cur_op)):
                nums_stack.append(cur_nums[j+1])
                op_stack.append(cur_op[j])
                if cur_op[j] == op:
                    num1 = nums_stack.pop()
                    num2 = nums_stack.pop()
                    cal = op_stack.pop()
                    ev = eval(f'{num2}{cal}{num1}')
                    nums_stack.append(ev)
            cur_nums = nums_stack[:]
            cur_op = op_stack[:]
        result = abs(nums_stack.pop())
        answer = max(answer, result)
    return answer


print(solution("100-200*300-500+20"))
