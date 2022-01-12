# 01/12
# 15650 N과M(2)

# 백트랙킹
N, M = map(int, input().split())

result = []


def Back(start):
    if len(result) == M:
        print(' '.join(map(str, result)))
    else:
        for i in range(start, N+1):
            if i not in result:
                #print(i, result)
                result.append(i)
                Back(i+1)
                result.pop()


Back(1)
