from collections import defaultdict


def solution(logs):
    answer = []
    dict = defaultdict()
    list = []

    for log in logs:
        user, num, score = log.split()
        dict[user] = []
        dict[user].append((num, score))

    print(dict)

    return answer


solution(["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80",
         "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"])
