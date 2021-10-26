# 10/26
# 3036 링
import math

N = int(input())
rings = list(map(int, input().split()))

first_ring = rings[0]
del rings[0]

# 기약분수 - 각 분모, 분자를 최대공약수로 나눈 수
for i in rings:
    gcd = math.gcd(first_ring, i)
    print(str(first_ring // gcd) + "/" + str(i // gcd))
