# 10/16
# 15649 N과M(1)

# 백트랙킹
N, M = map(int, input().split())

result = []


def Back():
    if len(result) == M:
        print(' '.join(map(str, result)))  # ' '와 join하기 위해 str로
    else:
        for i in range(1, N+1):
            # print(i)
            if i not in result:
                #print(i, result)
                result.append(i)
                Back()
                result.pop()


Back()
