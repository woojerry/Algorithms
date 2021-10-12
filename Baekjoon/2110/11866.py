# 10/12
# 11866 요세푸스 문제 0
from collections import deque
queue = deque()
answer = []

N, K = map(int, input().split())
for i in range(1, N+1):
    queue.append(i)

while queue:
    for _ in range(K-1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())

print("<", end="")
for j in range(len(answer) - 1):
    print(answer[j], end='')
    print(", ", end='')
print(answer[-1], end='')
print(">")
