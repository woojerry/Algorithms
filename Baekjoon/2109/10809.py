# 09/27
# 10809 알파벳 찾기

S = input()
for i in range(97, 123):  # 122가 z
    print(S.find(chr(i)))
