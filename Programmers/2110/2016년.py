
def solution(a, b):
    day_name = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 윤년이므로 2월은 29일까지
    days = 0
    for i in range(a-1):  # 0번째가 1월이므로
        days += month[i]
    answer = day_name[(days + b) % 7]
    return answer
