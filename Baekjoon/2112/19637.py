# 12/03
# 19637 if 문 좀 대신 써줘
import sys

read = sys.stdin.readline
N, M = map(int, read().split())
styles = []

for _ in range(N):
    style, standard = read().split()
    styles.append((style, int(standard)))


def binarysearch(left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if target <= styles[mid][1]:
            right = mid - 1
            answer = styles[mid][0]
        else:
            left = mid + 1

    return answer


for _ in range(M):
    power = int(read())
    print(binarysearch(0, N-1, power))
