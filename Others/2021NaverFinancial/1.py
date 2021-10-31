def solution(id_list, k):
    answer = 0
    dict = {}
    for i in id_list:
        ids = list(set(map(str, i.split())))
        for j in ids:
            if dict.get(j) == k:
                continue
            else:
                dict[j] = dict.get(j, 0) + 1
                answer += 1
    return answer


print(solution(["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY",
      "ELLE MAY", "ELLE ELLE ELLE", "MAY"], 3))
