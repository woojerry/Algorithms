# 01/24
# 1922 네트워크 연결
# 최소신장트리 - 크루스칼 알고리즘 -> 간선 정렬 + 유니온파인드(서로소)

N = int(input())
M = int(input())

parent = [0] * (N+1)
nodes = []


def find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]


def union(a, b):
    a_root = find(a)
    b_root = find(b)

    if a_root < b_root:
        parent[b_root] = a_root

    else:
        parent[a_root] = b_root


for _ in range(M):
    a, b, cost = map(int, input().split())
    nodes.append((a, b, cost))

nodes.sort(key=lambda x: x[2])
connect_count = 0
answer = 0  # 최소 비용

for i in range(1, N+1):
    parent[i] = i

for node in nodes:
    a, b, c = node
    #  현재 선택된 간선의 두개 정점이 연결된 상태가 아니라면 연결
    if find(a) != find(b):
        union(a, b)
        answer += c
        connect_count += 1

    if connect_count == N-1:
        break

print(answer)
