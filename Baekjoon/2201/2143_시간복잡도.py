# 01/18
# 2143 두 배열의 합
# 누적합 ,, 해시로 풂

import sys
read = sys.stdin.readline

T = int(read())
n = int(read())
A_list = list(map(int, read().split()))
m = int(read())
B_list = list(map(int, read().split()))
A_dic, B_dic = {}, {}


for i in range(n):
    sum_A = 0
    for j in range(i, n):
        sum_A += A_list[j]
        # 부분합 구하기 n(n+1)/2번 돌아감
        A_dic[sum_A] = A_dic.get(sum_A, 0) + 1

# 다른 방식으로 부분합 구하기
for i in range(m):
    sum_B = B_list[i]
    B_dic[sum_B] = B_dic.get(sum_B, 0) + 1
    for j in range(i+1, m):
        sum_B += B_list[j]
        B_dic[sum_B] = B_dic.get(sum_B, 0) + 1


answer = 0
for i in A_dic:
    if T-i in B_dic:
        answer += A_dic[i] * B_dic[T-i]
print(answer)

# 아래 코드는 시간초과
# for i in A_dic:
#     for j in B_dic:
#         if i+j == T:
#             answer += A_dic[i] * B_dic[j]
