# 11/01

def solution(str1, str2):
    answer = 0
    list1, list2 = [], []
    dic1, dic2 = {}, {}

    for i in range(len(str1)):
        if i == (len(str1) - 1):
            break
        if str1[i].isalpha() and str1[i+1].isalpha():
            two = str1[i].lower() + str1[i+1].lower()
            dic1[two] = dic1.get(two, 0) + 1

    for i in range(len(str2)):
        if i == (len(str2) - 1):
            break
        if str2[i].isalpha() and str2[i+1].isalpha():
            two2 = (str2[i].lower() + str2[i+1].lower())
            dic2[two2] = dic2.get(two2, 0) + 1

    union = 0
    intersection = 0
    for i in dic1.keys():
        if i in dic2:
            intersection += min(dic1[i], dic2[i])

    len1 = sum(dic1.values())
    len2 = sum(dic2.values())
    union = len1 + len2 - intersection

    if dic1 == {} and dic2 == {}:
        answer = 65536
    else:
        answer = int(intersection / union * 65536)

    return answer


print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
#print(solution("E=M*C^2", "e=m*c^2"))
