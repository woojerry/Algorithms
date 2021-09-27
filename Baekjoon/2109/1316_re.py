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
