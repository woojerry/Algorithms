# 10/12
# 1021 회전하는 큐

# 1. popleft()
# 2. append(popleft())
# 3. appendleft(pop())
from collections import deque

answer = 0
N, M = map(int, input().split())
queue = []
for i in range(1, N+1):
    queue.append(i)

find = list(map(int, input().split()))


deq = deque(i for i in queue)

for el in find:
    while True:
        if deq[0] == el:
            deq.popleft()
            break
        else:
            if deq.index(el) < (len(deq) / 2):  # index값이 곧 현재 배열값이므로
                deq.append(deq.popleft())
                answer += 1
            else:
                deq.appendleft(deq.pop())
                answer += 1

print(answer)
