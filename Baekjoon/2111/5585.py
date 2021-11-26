# 11/26
# 5585 거스름돈

price = int(input())

res = 1000 - price
money = [500, 100, 50, 10, 5, 1]
answer = 0
for i in money:
    count, res = divmod(res, i)
    answer += count
    if res == 0:
        break

print(answer)
