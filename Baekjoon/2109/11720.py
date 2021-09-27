# 09/27
# 11720 숫자의 합

N = int(input())
numbers = input()
sum = 0

for i in range(N):
    sum += int(numbers[i])
print(sum)
