from collections import defaultdict


def solution(logs):
    answer = []
    dic = defaultdict(dict)

    for log in logs:
        user, num, score = log.split()
        dic[user][num] = score

    print(dic)

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

solution(["1901 1 100", "1901 2 100", "1901 4 100", "1901 7 100", "1901 8 100", "1902 2 100", "1902 1 100", "1902 7 100", "1902 4 100", "1902 8 100", "1903 8 100", "1903 7 100",
         "1903 4 100", "1903 2 100", "1903 1 100", "1101 1 95", "1101 2 100", "1101 4 100", "1101 7 100", "1101 9 100", "1102 1 95", "1102 2 100", "1102 4 100", "1102 7 100", "1102 9 100"])

solution(["1901 10 50", "1909 10 50"])
