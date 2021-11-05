def solution(forms):
    answer = []
    word_cand = {}

    for member in forms:
        nickname = member[1]
        for i in range(len(nickname)-1):
            cand = nickname[i:i+2]
            word_cand[cand] = word_cand.get(cand, 0) + 1

    for member in forms:
        email, nickname = member[0], member[1]
        for i in range(len(nickname)-1):
            check = nickname[i:i+2]
            if word_cand[check] > 1:
                answer.append(email)
                break

    # for member in forms:
    #     email, nickname = member[0], member[1]
    #     for word in word_cand:
    #         if word_cand[word] > 1:
    #             if word in nickname:
    #                 answer.append(email)

    #answer = sorted(list(set(answer)))

    return sorted(answer)


print(solution([["jm@email.com", "제이엠"], ["jason@email.com", "제이슨"],
                ["woniee@email.com", "워니"], ["mj@email.com", "엠제이"], ["nowm@email.com", "이제엠"]]))
