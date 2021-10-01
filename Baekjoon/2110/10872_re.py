# 10/01
# 10872 팩토리얼

N = int(input())
result = 1


def factorial(n):
    if(n <= 1):
        return 1
    else:
        return n * factorial(n-1)


print(factorial(N))
