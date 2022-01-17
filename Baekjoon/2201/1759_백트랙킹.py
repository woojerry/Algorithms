# 01/17
# 1759 암호 만들기
# 백트랙킹

# 1. 체크인 - 생략 가능
# 2. 목적지인가? - 길이 + 자음,모음 개수
# 3. 연결된 곳을 순회 - 나보다 높은 알파벳
# 4. 갈 수 있는가? - 생략 가능
# 5. 간다 - dfs(next) => 자음, 모음
# 6. 체크아웃 - 생략 가능

# 사전순, # 최소 한개의 모음, 최소 두개의 자음, 길이
def Backtrack(length, start):
    if length == L:
        vowel_count = 0
        consonant_count = 0
        for i in range(L):
            if cand[i] in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

            if i == L-1 and vowel_count >= 1 and consonant_count >= 2:
                print(''.join(cand))

    for i in range(start, C):
        if visited[i]:
            continue
        visited[i] = True
        cand.append(alphabets[i])
        Backtrack(length+1, i)
        cand.pop()
        visited[i] = False


L, C = map(int, input().split())
alphabets = sorted(list(input().split()))

vowels = ["a", "e", "i", "o", "u"]
visited = [False] * C
cand = []

Backtrack(0, 0)
