# 03/10
# 10942 펠린드롬
import sys
read = sys.stdin.readline

N = int(read())
nums = list(map(int, read().split()))

M = int(read())
for _ in range(M):
    S, E = map(int, read().split())
