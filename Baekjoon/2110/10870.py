# 10/01
# 10870 피보나치 수

n = int(input())


def fibonacci(n):
    if(n >= 2):
        return fibonacci(n-2) + fibonacci(n-1)
    elif n == 1:
        return 1
    else:
        return 0


print(fibonacci(n))
