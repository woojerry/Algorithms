# 11/25
# 11728 배열 합치기
import sys

read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
A = list(map(int, read().rstrip().split()))
B = list(map(int, read().rstrip().split()))
answer = []

a, b = 0, 0
while a != len(A) or b != len(B):
    if a == len(A):
        answer.append(B[b])
        b += 1
    elif b == len(B):
        answer.append(A[a])
        a += 1
    else:
        if A[a] >= B[b]:
            answer.append(B[b])
            b += 1
        elif A[a] < B[b]:
            answer.append(A[a])
            a += 1

for i in answer:
    print(i, end=' ')
