# 1/1
# 5430 AC
from collections import deque


T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    error_detected = False
    nums_str = input()[1:-1].split(",")  # 음수 인덱싱 맨 뒤에 꺼 빼기
    if n == 0:
        nums = []
        for func in p:
            if func == 'D':
                print('error')
                error_detected = True
                break
        else:
            print('[]')
    else:
        # 문자열 deque에 넣기 -> 각 문자가 요소로 된 리스트 형태의 deque 생성
        nums = deque(nums_str)
        dir = True  # 정방향

        for func in p:
            if func == 'R':
                dir = not dir
            elif func == 'D':
                if len(nums) != 0:
                    if dir:
                        nums.popleft()
                    else:
                        nums.pop()
                else:
                    print('error')
                    error_detected = True
                    break

        if not error_detected:
            if not dir:
                nums.reverse()
            print("[" + ",".join(nums) + "]")
