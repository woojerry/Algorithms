# 10/16
# 15649 N과M(1)

# 백트랙킹
N, M = map(int, input().split())

result = []


def Back(depth):
    if depth == M:
        print(' '.join(map(str, result)))  # ' '와 join하기 위해 str로
    else:
        for i in range(1, N+1):
            if i not in result:
                result.append(i)
                Back(depth+1)
                result.pop()


Back(0)
