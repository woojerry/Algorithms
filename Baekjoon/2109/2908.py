# 09/27
# 2908 상수

A, B = input().split()  # 두 수 문자열로 입력받기

reversed_A = A[::-1]  # 거꾸로 뒤집기
reversed_B = B[::-1]

print(max(int(reversed_A), int(reversed_B)))
