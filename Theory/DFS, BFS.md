### 탐색
> 많은 양의 데이터 중 원하는 데이터를 찾는 과정
### 스택(Stack) 자료구조
> 먼저 들어온 데이터가 나중에 나가는 선입후출의 자료구조
- 파이썬에서는 리스트를 이용해 구현 가능.
```python
stack = []
stack.append(5) # 삽입(5)
stack.append(2) # 삽입(2)
stack.append(3) # 삽입(3)
stack.pop() # 삭제()
stack.append(1) # 삽입(1)

print(stack[::-1]) # 최상단 원소부터 출력 # [1,2,5]
print(stack) # 최하단 원소부터 출력 # [5,2,1]
```

### 큐(Queue) 자료구조
> 먼저 들어 온 데이터가 먼저 나가는 선입선출의 자료구조
- 파이썬에서는 리스트를 이용해 큐를 구현할 수 있지만, 그 경우 시간복잡도가 더 높아 비효율적으로 동작하므로 ```deque()``` 라이브러리를 사용
- deque 라이브러리에서 ```append()```는 리스트에서와 동일하게 동작하며, ```popleft```()는 가장 왼쪽에 있는 원소를 꺼낼 때 사용
```python
from collections import deque

# Queue 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5) 
queue.append(2)
queue.append(3)
queue.popleft() # 삭제()
queue.append(1) 

print(queue) # 먼저 들어온 순서대로 출력 # deque([2,3,1]
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력 # deque(1,2,3])
```

## DFS


