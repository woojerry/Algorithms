# 01/09
# 1159 농구 경기
# 해시맵

N = int(input())
dic = {}
for _ in range(N):
    first_name = input()[0]
    dic[first_name] = dic.get(first_name, 0) + 1

str = []
for i in dic.keys():
    if dic[i] >= 5:
        str.append(i)
str.sort()


if len(str) == 0:
    print('PREDAJA')
else:
    answer = ''
    for j in str:
        answer += j
    print(answer)
