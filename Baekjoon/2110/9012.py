# 10/15
# 9012 괄호

T = int(input())

for _ in range(T):
    string = input()
    stack = []
    for i in string:
        if i == "(":
            stack.append("(")
        else:  # i == ")"
            if len(stack) == 0:
                stack.append(")")
                break
            stack.pop()
    if len(stack) > 0:
        print("NO")
    else:
        print("YES")
