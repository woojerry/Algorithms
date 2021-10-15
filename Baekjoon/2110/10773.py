# 10/15
# 10773 제로

K = int(input())
stack = []
for _ in range(K):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

sum = 0
for i in stack:
    sum += i

print(sum)
