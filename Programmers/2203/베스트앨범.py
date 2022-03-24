# 03/24
# 해시 + 정렬

def solution(genres, plays):
    answer = []

    dic = {}
    dic2 = {name: [] for name in set(genres)}

    for i in range(len(genres)):
        dic[genres[i]] = dic.get(genres[i], 0) + plays[i]
        dic2[genres[i]].append((plays[i], i))

    print(dic)
    print(dic2)

    popular_genres = sorted(dic.items(), key=lambda x: -x[1])
    print(popular_genres)

    for genre, _ in popular_genres:
        print(sorted(dic2[genre], key=lambda x: (-x[0], x[1]))[:2])
        for _, song_num in sorted(dic2[genre], key=lambda x: (-x[0], x[1]))[:2]:
            answer.append(song_num)

    return answer
