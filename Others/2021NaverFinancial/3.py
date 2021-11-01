from collections import defaultdict


def solution(logs):
    answer = []
    dic = defaultdict(dict)

    for log in logs:
        user, num, score = log.split()
        dic[user][num] = score

    for i in dic:
        for j in dic:
            if i == j:
                continue
            if len(dic[i]) > 4 and len(dic[i]) == len(dic[j]):
                for k in dic[i].keys():
                    if k in dic[j] and dic[i][k] == dic[j][k]:
                        pass
                answer.append(i)
                answer.append(j)

    if answer != []:
        print(sorted(list(set(answer))))
    else:
        print(["None"])
    return answer


solution(["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80",
         "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"])

solution(["1901 10 50", "1909 10 50"])
