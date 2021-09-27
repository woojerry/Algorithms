numbers = set(range(1, 10001))
not_self_numbers = set()


def d(n):  # d(n)함수
    for i in str(num):
        n += int(i)
    return n


for num in (numbers):
    not_self_numbers.add(d(num))

self_numbers = numbers - not_self_numbers  # 차집합 이용

for i in sorted(self_numbers):  # 오름차순 정렬
    print(i)
