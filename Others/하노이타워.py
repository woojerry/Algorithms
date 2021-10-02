# 하노이는 불교 순례지로 유명한 이야기가 내려옵니다.
# 땡중들이 노름하고 있어서 이를 본 부처가 푼 돈 가지고 놀음하냐고 놀려댑니다.
# A 기둥에 64개의 원판(순금)이 있는데 B 기둥을 이용해서 C기둥에 이동시키면
# 모두 주겠다고 말합니다.
# 원판은 하나씩 이동시켜야 하며, 큰 원판 위에 작은 원판을 놓을 수 있다.


# 입력은 세 개의 기둥과 움직여야 할 돌의 개수
# 출력은 돌의 이동하는 순서 목록
# 입력: ["A","B","C",3]
# 출력: [["A","C"],["A","B"],["C","B"],["A","C"],["B","A"],["B","C"],["A","C"]]

def Hanoi(src, use, dst, n):
    path = []
    if(n <= 0):
        return path
    if(n == 1):
        path.append([src, dst])
    else:
        p1 = Hanoi(src, dst, use, n-1)
        path.extend(p1)
        path.append([src, dst])
        p2 = Hanoi(use, src, dst, n-1)
        path.extend(p2)
    return path


print(Hanoi("A", "B", "C", 3))
