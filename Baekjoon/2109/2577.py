# 0929
# 숫자의 개수

A = int(input())
B = int(input())
C = int(input())
multiple = A * B * C

for i in range(0, 10):
    count = str(multiple).count(str(i))
    print(count)
