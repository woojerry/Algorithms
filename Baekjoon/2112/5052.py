# 12/11
# 5052 전화번호 목록
import sys
read = sys.stdin.readline


def check_consistency(phone_book_list):
    for phone_nums in phone_book_list:
        tmp = ''
        for j in phone_nums:
            tmp += j
            if tmp in dic and tmp != phone_nums:
                return "NO"
    return 'YES'


t = int(read())
for _ in range(t):
    N = int(read())
    phone_book = []
    dic = {}
    for _ in range(N):
        phone_num = str(read().rstrip())
        phone_book.append(phone_num)
        dic[phone_num] = dic.get(phone_num, 0) + 1
    print(check_consistency(phone_book))
