# 1110 더하기 사이클

N = int(input())
new = N
cycle = 0

while(True):
    sum = (new // 10) + (new % 10)
    new = (new % 10) * 10 + sum % 10
    cycle += 1
    if(new == N):
        print(cycle)
        break
