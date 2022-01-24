# 어떤 수 n을 2부터 루트(n)까지 나눈 나머지가 모두 0이 아님을 확인
def is_prime(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5)+1):
            if num % i == 0:
                return False
        return True
