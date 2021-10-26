# 10/26 나이순 정렬
# 10814
# 입력받은 순 = 가입한 순 ? 정렬은?

N = int(input())
answer = []

for _ in range(N):
    age, name = input().split()
    answer.append((int(age), name))

answer.sort(key=lambda x: (x[0]))  # 나이 기준으로 오름차순 정렬

for i in answer:
    print(i[0], i[1])
