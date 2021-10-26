from collections import deque
from datetime import datetime


def solution(totalTickets, logs):
    queue = deque(logs)
    answer = []

    recent_user = logs[0].split()[0]
    recent_time = logs[0].split()[2]
    answer.append(recent_user)
    queue.popleft()

    while(queue):
        user, action, time = queue.popleft().split()

        # if 아이디가 이전과 같고 (leave고) 시간이 1분이내면 예매불가
        if user == recent_user and action == 'leave':
            if int((datetime.strptime(time, "%H:%M:%S") - datetime.strptime(recent_time, "%H:%M:%S")).seconds) <= 60:
                answer.pop()
                continue

        # 아이디가 다르고 시간이 1분 이내면 예매불가
        elif user != recent_user and int((datetime.strptime(time, "%H:%M:%S") - datetime.strptime(recent_time, "%H:%M:%S")).seconds) <= 60:
            continue

        # 아니면 예매 가능
        else:
            answer.append(user)
            recent_user = user
            recent_time = time

    # id는 오름차순으로 정렬해 return
    answer.sort()
    return answer


print(solution(2000, ["woni request 09:12:29", "brown request 09:23:11", "brown leave 09:23:44",
      "jason request 09:33:51", "jun request 09:33:56", "cu request 09:34:02"]))
