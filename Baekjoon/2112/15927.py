# 12/10
# 15927 회문은 회문아니야!

string = input()  # 500,000
is_all_same = True
is_palindrome = True
for i in range(1, len(string)-1):
    if string[0] != string[i]:
        is_all_same = False
        break

for j in range(len(string) // 2):
    if string[j] != string[-1 - j]:
        is_palindrome = False
        break

if is_palindrome:
    if is_all_same:
        answer = -1
    else:
        answer = len(string) - 1
else:
    answer = len(string)

print(answer)
