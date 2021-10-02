# 언휴는 피연산자는 정수이고 사칙 연산을 수행하는 계산기를 만들려고 합니다.
# 그런데 “2+3*5-7” 처럼 수식을 입력하였을 때 순차적으로 연산을 수행하면 연산자 우선 순위 때문에 이상한 결과를 내는 것을 발견했어요.
# 언휴는 연구 끝에 두 개의 피연산자를 먼저 표기하고 연산 기호를 뒤에 표기하는 후위 수식 표기를 사용하면 원하는 결과를 얻어낼 수 있다는 것을 알게 되었어요.
# (피연산자를 만나면 스택에 보관하고 연산자를 만나면 두 번 꺼내어 연산한 값을 다시 스택에 보관하면 마지막에 남은 값이 연산 결과입니다.)
# 언휴는 사용자가 입력한 수식을 피연산자와 연산자로 분리하여 토큰 배열을 만들었어요.
# 여러분은 언휴를 도와 토큰 배열을 입력 인자로 전달받아 계산하는 코드를 작성하세요.

# 입력은 수식 토큰(후위 표기 순서)
# 출력은 계산 결과
# 입력: {“2”, “3”, “5”, “*”, “+”, “7”, “-“}
# 출력:  9

def Calculate(tokens):
    stack = []
    for token in tokens:
        if token == "+":
            rv = stack.pop()
            lv = stack.pop()
            stack.append(lv+rv)
        elif token == "-":
            rv = stack.pop()
            lv = stack.pop()

            stack.append(lv-rv)
        elif token == "*":
            rv = stack.pop()
            lv = stack.pop()

            stack.append(lv * rv)
        elif token == "/":
            rv = stack.pop()
            lv = stack.pop()

            stack.append(lv / rv)
        else:
            stack.append(int(token))
    return stack.pop()


print(Calculate(["2", "3", "5", "*", "+", "7", "-"]))
