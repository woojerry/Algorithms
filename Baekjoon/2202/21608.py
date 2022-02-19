# 02/18
# 21608 상어 초등학교
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

N = int(input())
classroom = [[0] * N for _ in range(N)]
students = []
for _ in range(N*N):
    tmp = list(map(int, input().split()))
    students.append((tmp[0], tmp[1:]))
    
