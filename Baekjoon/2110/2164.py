# 10/12
# 2164 카드2
from collections import deque

N = int(input())
queue = deque()

for i in range(1, N+1):
    queue.append(i)  # 카드 넣기

while len(queue) != 1:
    queue.popleft()
    second = queue.popleft()
    queue.append(second)
print(queue[0])
