# 11/24
# 7453 합이 0인 네 정수
import sys

read = sys.stdin.readline
n = int(read())

A, B, C, D = [0]*n, [0]*n, [0]*n, [0]*n
for i in range(n):
    A[i], B[i], C[i], D[i] = map(int, read().rstrip().split())

AB = {}

for j in range(n):
    for k in range(n):
        AB[A[j] + B[k]] = AB.get(A[j] + B[k], 0) + 1

count = 0
for x in range(n):
    for y in range(n):
        count += AB.get(-(C[x] + D[y]), 0)

print(count)
