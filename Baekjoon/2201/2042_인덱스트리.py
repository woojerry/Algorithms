# 01/20
# 2042 구간 합 구하기
# 세그먼트 트리 O(logN), Top-down

import sys
read = sys.stdin.readline


def init(node, start, end):
    # node가 리프 노드인 경우 배열의 원소 반환
    if start == end:  # start == end -> leaf node
        tree[node] = array[start]
        return tree[node]
    else:  # 재귀 함수를 이용해서 왼쪽 자식과 오른쪽 자식 트리를 만들고, 그 합을 저장
        tree[node] = init(node*2, start, (start+end) // 2) + \
            init(node*2+1, (start+end)//2 + 1, end)
        return tree[node]


def query(node, start, end, left, right):
    if left > end or right < start:
        return 0


N, M, K = map(int, read().split())
array = []
tree = [0] * N * 4  # 최대 4N개
for _ in range(N):
    array.append(int(read()))

init(1, 0, N-1)
