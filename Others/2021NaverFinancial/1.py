def solution(id_list, k):
    answer = 0
    dic = {}
    for i in id_list:
        ids = list(set(map(str, i.split())))
        for j in ids:
            if dic.get(j) == k:
                continue
            else:
                dic[j] = dic.get(j, 0) + 1
                answer += 1
    return answer


print(solution(["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY",
      "ELLE MAY", "ELLE ELLE ELLE", "MAY"], 3))
