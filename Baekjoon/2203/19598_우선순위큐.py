# 04/01
# 19598 최소 회의실 개수
import heapq
import sys
read = sys.stdin.readline

N = int(read())
times = []
for _ in range(N):
    st, ed = map(int, read().split())
    times.append((st, ed))


times.sort(key=lambda x: x[0])

rooms = [0]
answer = 1
for st, ed in times:
    if st >= rooms[0]:
        heapq.heappop(rooms)
    else:
        answer += 1

    heapq.heappush(rooms, ed)

print(answer)
