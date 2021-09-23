# 1330 두 수 비교하기

A, B = map(int, input().split())  # 입력받은 값을 공백을 기준으로 분리

if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")
