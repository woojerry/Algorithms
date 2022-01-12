# 01/12
# 15651 N과M(3)

# 백트랙킹
N, M = map(int, input().split())

result = []


def Back():
    if len(result) == M:
        print(' '.join(map(str, result)))
    else:
        for i in range(1, N+1):
            # if i not in result:
            result.append(i)
            Back()
            result.pop()


Back()
