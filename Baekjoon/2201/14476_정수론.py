# 01/20
# 14476 최대공약수 하나 빼기
# 유클리드 호제법 + 누적 최대공약수 -> 시간복잡도 O(N)으로
# 왼쪽에서 오른쪽까지의 최대 공약수 누적으로 계산해서 저장
# 마찬가지로 오른쪽에서 왼쪽도 누적 계산해 1개 제외했을 때 값 구하기

import sys
read = sys.stdin.readline

N = int(read())
numbers = list(map(int, read().split()))


def gcd(a, b):  # a > b일 때
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


left_right = [0] * (N+1)
right_left = [0] * (N+1)

left_right[0] = numbers[0]
right_left[N-1] = numbers[N-1]

max, max_index = 0, 0
for i in range(1, N):
    left_right[i] = gcd(left_right[i-1], numbers[i])

for j in range(N-2, -1, -1):
    right_left[j] = gcd(right_left[j+1], numbers[j])

for k in range(N):
    tmp = 0
    if k == 0:  # 왼쪽 끝
        tmp = right_left[1]
    elif k == N-1:
        tmp = left_right[N-2]
    else:
        tmp = gcd(left_right[k-1],  right_left[k+1])

    if numbers[k] % tmp == 0:  # k가 gcd로 나눠지면 안되므로
        continue

    if tmp > max:
        max = tmp
        max_index = k

if max == 0:
    print(-1)
else:
    print(max, numbers[max_index])
