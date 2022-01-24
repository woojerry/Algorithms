# 01/24
# 1717 집합의 표현
# 서로소 집합(유니온)

import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline

n, m = map(int, read().split())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i


def find(a):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[a] == a:  # 자기자신이 루트노드일 때
        return a
    else:  # 루트노드가 아니라면 루트노드를 찾을 때까지 재귀적으로 호출한 뒤에 부모값 갱신 -> 시간복잡도 개선
        parent[a] = find(parent[a])
        return parent[a]


def union(a, b):
    a_root = find(a)
    b_root = find(b)

    if a_root < b_root:  # 더 작은 것을 루트로 설정하는 것
        parent[b_root] = a_root

    else:
        parent[a_root] = b_root


for _ in range(m):
    type, a, b = map(int, read().split())
    if type == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
