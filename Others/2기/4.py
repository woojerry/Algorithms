def solution(infos, actions):
    db = {}
    answer = []
    login = False
    added = False
    for info in infos:
        id, pwd = info.split()
        db[id] = pwd

    for action in actions:
        do = action.split()[0]
        if do == "ADD":
            if login:
                answer.append(True)
                added = True
            else:
                answer.append(False)
        elif do == "LOGIN":
            if login:
                answer.append(False)
            else:
                id, pwd = action.split()[1], action.split()[2]
                if id not in db:
                    answer.append(False)
                    continue
                if db[id] != pwd:
                    answer.append(False)
                elif db[id] == pwd:
                    answer.append(True)
                    login = True
        elif do == "ORDER":
            if added:
                answer.append(True)
                added = False
            else:
                answer.append(False)

    return answer


print(solution(["kim password", "lee abc"], ["ADD 30", "LOGIN kim abc", "LOGIN lee password",
      "LOGIN kim password", "LOGIN kim password", "ADD 30", "ORDER", "ORDER", "ADD 40", "ADD 50"]))
