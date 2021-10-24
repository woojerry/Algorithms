# 10/18
# 2608 로마 숫자

roman = {"I": 1,  "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50,
         "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}

roman_1 = input()
roman_2 = input()


def roman_to_num(roman_num):
    number = 0
    for i in range(len(roman_num)):
        if i+1 == len(roman_num):
            number += roman[roman_num[i]]
            break
        else:
            if roman[roman_num[i]] >= roman[roman_num[i+1]]:
                number += roman[roman_num[i]]
            else:
                number -= roman[roman_num[i]]
    return number


sum = roman_to_num(roman_1) + roman_to_num(roman_2)

print(sum)

to_int = {v: k for k, v in roman.items()}
to_int_list = reversed(list(to_int.keys()))
answer = ''

while sum > 0:
    for i in to_int_list:
        cnt, sum = divmod(sum, i)
        answer += to_int[i] * cnt
print(answer)
