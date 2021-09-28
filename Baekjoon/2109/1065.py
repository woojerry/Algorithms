# 09/28
# 1065 한수

# 한수: 어떤 양의 정수 X의 각 자리가 등차수열을 이룰 때 그것이 한수
# 등차수열: 연속된 두 개의 수의 차이가 일정한 수열

N = int(input())
count = 0  # 한수의 개수

if N > 99:  # 3자리수
    count = 99
    numbers = set(range(100, N+1))
    numbers_list = list(numbers)

    for i in numbers_list:
        string_num = str(i)
        if(int(string_num[2]) - int(string_num[1]) == int(string_num[1]) - int(string_num[0])):
            count += 1

else:  # 1 ~ 99까지는 모두 한수
    count = N

print(count)

# nums = list(map(int, str(n)))  # 숫자를 자릿수대로 분리
