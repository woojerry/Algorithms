# 09/27
# 1316 그룹 단어 체커

N = int(input())
group_word_cnt = N
for _ in range(N):
    word = input()
    already = []
    for i in range(len(word)):
        if word[i] in already:
            group_word_cnt -= 1
            break

        if i != len(word)-1:
            if word[i] == word[i+1]:
                pass
            elif word[i] != word[i+1]:
                already.append(word[i])

print(group_word_cnt)


# 다른 풀이
# for-else문 사용: 중간에 break 걸리면 else문 실행 X
N = int(input())
ans = 0
for _ in range(N):
    string = input()
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            pass
        elif string[i] in string[i + 1:]:  # 현재글자 이후 문자열을 확인
            break
    else:  # break에 안걸렸을 때 그룹 단어의 개수 증가 시킴
        ans += 1
print(ans)
