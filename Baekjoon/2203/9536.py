# 03/01
# 9536 여우는 어떻게 울지?

T = int(input())
for _ in range(T):
    dic = {}
    sounds = list(map(str, input().split()))
    for i in sounds:
        dic[i] = dic.get(i, 0) + 1
        
    while True:
        tmp = str(input())
        if tmp == 'what does the fox say?':
            break
        else:
            _, _ , s = tmp.split()
            for _ in range(dic[s]):
                sounds.remove(s)
 
    for i in sounds:
        print(i, end=' ')