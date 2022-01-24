# 10진수 -> n진수 (2진수-16진수)

def convert_notation_from_decimal(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)

    # str로 반환
    return convert_notation_from_decimal(q, base) + T[r] if q else T[r]


print(convert_notation_from_decimal(233, 3))
