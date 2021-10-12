# 10/12
# 7568 덩치

N = int(input())
people = []
answer = []

for _ in range(N):
    x, y = map(int, input().split())
    people.append((x, y))

for i in people:
    rank = 1
    for j in people:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    answer.append(rank)

for rank in answer:
    print(rank, end=' ')
