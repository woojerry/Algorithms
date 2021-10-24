# 10/18
# 1920 수 찾기
# 해시

N = int(input())
dict = {}
range_num = list(map(int, input().split()))
for i in range_num:
    dict[i] = dict.get(i, 0) + 1

M = int(input())
check_num = list(map(int, input().split()))

for j in range(M):
    if check_num[j] in dict:
        print(1)
    else:
        print(0)
