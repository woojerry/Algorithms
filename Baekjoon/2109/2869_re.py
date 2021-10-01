# 09/29
# 2869 달팽이는 올라가고 싶다
# 시간 제한: 0.15초

# 시간제한이 있으므로, 시간복잡도가 O(1)이어야 함 -> 연산으로 풀기
import math

A, B, V = map(int, input().split())

if (V-A) % (A-B) == 0:
    days = (V-A) / (A-B) + 1
else:
    days = math.ceil((V-A) / (A-B)) + 1
print(int(days))
