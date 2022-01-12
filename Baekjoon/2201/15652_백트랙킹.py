# 01/12
# 15651 N과M(4)

# 백트랙킹
N, M = map(int, input().split())

result = []


def Back(start):
    if len(result) == M:
        print(' '.join(map(str, result)))

    else:
        for i in range(start, N+1):
            result.append(i)
            Back(i)
            result.pop()


Back(1)
