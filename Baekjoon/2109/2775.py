# 2775 부녀회장이 될테야

# 0층 ~ 14층  # 1호 ~ 14호
apartment = [[0] * 15 for _ in range(15)]

for i in range(1, 15):  # 0층
    apartment[0][i] = i

for i in range(1, 15):  # 1층 ~ 14층
    for j in range(1, 15):  # 1호 ~ 14호
        apartment[i][j] = apartment[i-1][j] + apartment[i][j-1]
        #apartment[i][j] = sum(apartment[i-1][1 : j+1])

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(apartment[k][n])
