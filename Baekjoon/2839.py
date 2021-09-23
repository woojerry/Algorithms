# 2839 설탕 배달

sugar = int(input())
result = 0

while(True):
    if sugar % 5 == 0:
        result += sugar // 5
        print(result)
        break
    sugar -= 3
    result += 1
    if(sugar < 0):
        print(-1)
        break
