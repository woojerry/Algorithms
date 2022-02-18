# 02/18
# 수식찾기 + 완전탐색

# 가로: x, 세로: y
# xy = brown * yellow
# 2x + 2y -4 = brown

def solution(brown, yellow):
    total = brown + yellow
    for x in range(1, total +1):
        if total % x == 0:
         y = total // x
         if x >= y:
             if 2*x + 2*y -4 == brown:
                 answer = [x,y]
    
    return answer