# 11/17
# 회사에 있는 사람

n = int(input())

dic = {}
for _ in range(n):
    name, action = input().split()
    if action == "enter":
        dic[name] = dic.get(name, 0) + 1
    else:
        dic.pop(name)

answer = []
for i in dic.keys():
    answer.append(i)

answer = sorted(answer, reverse=True)
for j in answer:
    print(j)
