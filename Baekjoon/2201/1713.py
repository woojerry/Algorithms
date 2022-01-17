# 01/07
# 1317 후보 추천하기
# 정렬

N = int(input())
total = int(input())
recommends = list(map(int, input().split()))
dict = {}

for i in range(total):
    if len(dict) == N:
        if recommends[i] in dict:
            dict[recommends[i]][0] += 1
        else:
            # 개수가 같을 때 안정정렬
            least = (sorted(dict.items(), key=lambda x: (
                x[1][0], x[1][1]))[0][0])

            del dict[least]
            dict[recommends[i]] = [1, i]  # 순서까지 저장

    else:
        if recommends[i] in dict:
            dict[recommends[i]][0] += 1
        else:
            dict[recommends[i]] = [1, i]

print(' '.join(map(str, sorted(dict.keys()))))
