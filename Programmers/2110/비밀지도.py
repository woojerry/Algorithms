def change_to_bit(num, n):
    arr = []
    if num <= 1:
        arr.append(str(num))
    else:
        while(True):
            if(num <= 1):
                break
            arr.append(str(num % 2))
            num = num // 2

        arr.append('1')
    if len(arr) != n:
        for _ in range(n-len(arr)):
            arr.append('0')
    arr.reverse()
    result = "".join(arr)
    return result


def solution(n, arr1, arr2):
    get_or = []
    answer = []
    for i in range(len(arr1)):
        arr1[i] = (change_to_bit(arr1[i], n))
        arr2[i] = (change_to_bit(arr2[i], n))
        tmp = []
        for j in range(n):
            tmp.append(str((int(arr1[i][j]) | int(arr2[i][j]))))
        get_or.append("".join(tmp))

    for k in range(len(arr1)):
        get_or[k] = get_or[k].replace('0', " ")
        get_or[k] = get_or[k].replace('1', "#")
        answer.append(get_or[k])

    return answer
