# 10/12
# 2231 분해합

N = int(input())

answer = 0

for i in range(1, N):
    num = list(map(int, str(i)))  # 문자열도 iterable객체
    find = i + sum(num)
    if find == N:
        answer = i
        break

print(answer)
