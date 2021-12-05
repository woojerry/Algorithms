def solution(name):
    answer = 0
    alphabets = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11,
                 "M": 12, "N": 13, "O": 12, "P": 11, "Q": 10, "R": 9, "S": 8, "T": 7, "U": 6, "V": 5, "W": 4, "X": 3, "Y": 2, "Z": 1}

    location = 1
    up_down = []
    for i in name:
        up_down.append(alphabets[i])

    # for i in range(len(name)):
    #     name[i]
    for j in name:
        if j == 'A':
            count_A = 1
            for k in range(j, len(name)-1):
                if name[k] == 'A':
                    count_A += 1
                else:
                    break
            # 뒤에서부터 가는거리와 바로 가는 거리의 최소값..

    # 알파벳의 값 ..
    # A는 무시 .. default
    # continue 활용 ..? 기준 N

    return answer


print(solution('JAZ'))
