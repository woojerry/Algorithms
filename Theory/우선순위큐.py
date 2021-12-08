# 우선순위 큐(Priority Queue) - 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조

# 우선순위 큐 구현 방식
# 리스트 - 삽입: O(1), 삭제 O(N)
# 힙(Heap) - 삽입: O(logN), 삭제 O(logN)

# 힙정렬: O(NlogN)

import heapq  # minheap


def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        # heappop 함수는 가장 작은 원소를 힙에서 제거함과 동시에 그를 결괏값으로 리턴
        result.append(heapq.heappop(h))
    return result


n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

res = heapsort(arr)

for i in range(n):
    print(res[i])
