# 10진수 -> n진수 (2진수-16진수)

def convert_notation(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)

    return convert_notation(q, base) + T[r] if q else T[r]


print(convert_notation(233, 3))
