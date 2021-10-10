# 10/10

def solution(record):
    answer = []

    user = {}
    for words in record:
        if words.split()[0] == "Leave":
            continue
        else:
            action, uid, nickname = words.split()
            user[uid] = nickname

    for words in record:
        uid = words.split()[1]
        if words.split()[0] == "Change":
            continue
        elif words.split()[0] == "Enter":
            action = "님이 들어왔습니다."
        else:
            action = "님이 나갔습니다."

        message = user[uid] + action
        answer.append(message)

    return answer
