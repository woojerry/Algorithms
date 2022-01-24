def check_prime(num):
    is_prime = [True] * (num+1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(num ** 0.5) + 1):
        if is_prime[i] == True:
            for j in range(2 * i, num+1, i):
                is_prime[j] = False

    print(is_prime)
    return is_prime[num]


print(check_prime(12))
