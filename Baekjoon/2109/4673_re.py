# 4673 셀프 넘버

numbers = set(range(1, 10001))
not_self_numbers = set()


def d(num):  # d(n): n과 n의 각 자리수를 더하는 함수
    sum = num
    for i in str(num):
        sum += int(i)
    return sum


for num in (numbers):
    not_self_numbers.add(d(num))

self_numbers = numbers - not_self_numbers  # 차집합 이용

for i in sorted(self_numbers):  # 오름차순 정렬
    print(i)
