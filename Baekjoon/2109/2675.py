# 09/27
# 2675 문자열 반복

T = int(input())  # 테스트 케이스의 개수

for _ in range(T):
    R, S = input().split()  # R:반복횟수, S:문자열
    P = ''
    for i in S:
        tmp = i * int(R)
        P += tmp
    print(P)
