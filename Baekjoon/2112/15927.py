# 12/10
# 15927 회문은 회문아니야!

string = input().strip()  # 500,000

is_palindrome = True
is_all_same = True
for i in range(len(string) // 2):
    if string[i] != string[-1 - i]:
        is_palindrome = False
        break

if string == string[0] * len(string):
    is_all_same = False

if is_palindrome:
    if is_all_same:
        answer = -1
    else:
        answer = len(string) - 1

else:
    answer = len(string)

if len(string) == 1:
    answer = -1

# for j in range(len(string)):
#     if j == 0:
#         continue
#     word += string[j]
#     print(word)
#     if palindrome(word):
#         answer = max(answer, len(word)-1)
#         #word = ''
#         not_palindrome = 0
#     else:
#         if j == len(string):
#             answer = max(answer, len(word))

#     # else:
#     #     not_palindrome += 1

#     # if not_palindrome == len(string):
#     #     answer = not_palindrome

#     # print(answer)
#     if j == len(string)-1 and answer == 0:
#         answer = -1

print(answer)
