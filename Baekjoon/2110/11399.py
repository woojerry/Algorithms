# 10/07
# 11399 ATM

N = int(input())  # 사람의 수
people = list(map(int, input().split()))

people.sort()
result = 0
previous = 0
for i in people:
    result += i + previous
    previous += i

print(result)
