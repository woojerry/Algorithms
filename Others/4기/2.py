from datetime import datetime


def to_minutes(time):
    hours, minutes = map(int, time.split(":"))
    return hours * 60 + minutes


def to_time(minutes):
    hours, minutes = map(str, divmod(minutes, 60))
    hours = "0" * (2 - len(hours)) + hours
    return f"{hours}:{minutes}"


def solution(log):
    answer = ''
    acc = 0

    for i in range(len(log)):
        if i % 2 == 0:  # 시작시간
            start = to_minutes(log[i])

        else:  # 중지 시각
            end = to_minutes(log[i])
            diff = end - start
            if diff > 105:
                acc += 105
            elif diff < 5:
                acc += 0
            else:
                acc += diff

    answer = to_time(acc)

    return answer


print(solution(["08:30", "09:00", "14:00", "16:00",
      "16:01", "16:06", "16:07", "16:11"]))
