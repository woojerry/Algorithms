# 0928
# 2750 수 정렬하기

N = int(input())
numbers = list()

for _ in range(N):
    number = int(input())
    numbers.append(number)

sorted_numbers_list = sorted(numbers)

for i in sorted_numbers_list:
    print(i)
