import math


def solution(names, homes, grades):
    li = []
    for i in range(len(names)):
        distance = int(math.pow(homes[i][0], 2)) + \
            int(math.pow(homes[i][1], 2))
        li.append([int(str(grades[i]).split('.')[0]), distance, names[i]])

    li.sort(key=lambda x: (-x[0], -x[1], x[2]), )
    # dic = {}
    # for j in range(len(li)):
    #     dic[li[j][2]] = j+1

    dic = {li[j][2]: j+1 for j in range(len(li))}
    # for k in names:
    #     answer.append(dic[k])
    answer = [dic[k] for k in names]

    return answer


print(solution(["azad", "andy", "louis", "will", "edward"], [
      [3, 4], [-1, 5], [-4, 4], [3, 4], [-5, 0]], [4.19, 3.77, 4.41, 3.65, 3.58]))
