# 10/19
# 1181 단어 정렬

N = int(input())

word_list = []
for _ in range(N):
    word = str(input())
    word_list.append(word)

word_list = list(set(word_list))  # set은 순서가 없으므로 먼저 중복제거

word_list_with_length = []
for i in word_list:
    word_list_with_length.append((len(i), i))


word_list_with_length.sort(key=lambda x: (x[0], x[1]))


for i in range(len(word_list_with_length)):
    print(word_list_with_length[i][1])
