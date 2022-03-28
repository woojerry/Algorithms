# 01/27
# 풀긴 풀었으나 코드가 지저분 -> 리팩토링
# 해시, 딕셔너리 컴프리헨션

def solution(id_list, report, k):
    answer = []
    filtered_report = list(set(report))

    dictionary = {name: [] for name in id_list}
    dictionary2 = {name: 0 for name in id_list}

    print(dictionary)
    print(dictionary2)

    for i in filtered_report:
        a, b = i.split()
        dictionary[a].append(b)
        dictionary2[b] += 1

    out = []
    for i in dictionary2:
        if dictionary2[i] >= k:
            out.append(i)

    for id in id_list:
        tmp = 0
        for i in dictionary[id]:
            if i in out:
                tmp += 1
        answer.append(tmp)

    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], [
      "muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
