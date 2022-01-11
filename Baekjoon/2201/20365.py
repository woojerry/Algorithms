# 01/11
# 20365

N = int(input())
questions = list(input())
blue, red = 0, 0


cont = 1
for question in questions:
    if question == 'B':
        blue += 1
    else:
        red += 1

if blue > red:
    pivot = 'B'
elif red > blue:
    pivot = 'R'
else:
    pivot = questions[0]

answer = 1
continuous = False

for i in range(N):
    if not continuous:
        if questions[i] == pivot:
            continue
        else:  # pivot이랑 다를경우
            continuous = True
            answer += 1
    else:  # continous
        if questions[i] == pivot:
            continuous = False

    print(answer, i)

print(answer)
