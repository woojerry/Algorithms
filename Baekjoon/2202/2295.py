# 02/08
# 2295 세 수의 합
n = int(input())

u = set()
for i in range(n):
    u.add(int(input()))

a_b_sums = set()
for i in u:
    for j in u:
        a_b_sums.add(i + j)

ans = {}
for i in u:
    for j in u:
        if (i - j) in a_b_sums:
            ans[i] = (i, j, i - j)

keys = list(ans.keys())
keys.sort(reverse=True)
print(ans)
print(keys[0])
