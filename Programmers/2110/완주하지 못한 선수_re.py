# 10/14

# collections Counter객체 사용한 경우
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


# dict를 이용한 풀이


def solution(participant, completion):
    answer = ''
    dict = {}
    for i in participant:
        dict[i] = dict.get(i, 0) + 1

    for j in completion:
        dict[j] -= 1

    for key in dict:
        if dict[key] != 0:
            answer = key

    return answer


# 해시를 쓰지 않은 경우 - 효율성 테스트 실패


def solution(participant, completion):
    for i in range(len(completion)):
        if completion[i] in participant:
            participant.remove(completion[i])
    answer = participant[0]
    return answer
