import sys

read = sys.stdin.readline
N = int(read())
skills = sorted(list(map(int, read().rstrip().split())))
count = 0
skill_sum = 0

for pick in range(N):
    if skills[pick] > 0:  # 정렬돼있으므로
        break
    start, end = pick + 1, N-1
    j = N
    while start < end:
        skill_sum = skills[pick] + skills[start] + skills[end]
        if skill_sum == 0:
            if skills[start] == skills[end]:  # start와 end가 서로 같을 때
                count += (end - start + 1)*(end - start) // 2
                break

            else:  # start와 end가 다를 때
                start_same, end_same = 0, 0
                start_data, end_data = skills[start], skills[end]
                while True:
                    if skills[end] == end_data:
                        end_same += 1
                        end -= 1
                    else:
                        break
                while True:
                    if skills[start] == start_data:
                        start_same += 1
                        start += 1
                    else:
                        break
                count += start_same * end_same

        elif skill_sum > 0:
            end -= 1
        else:
            start += 1
print(count)
