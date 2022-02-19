# 02/19
# 3040 백설 공주와 일곱 난쟁이

cands = []
for _ in range(9):
    cands.append(int(input()))
    
total = sum(cands)
    
found = False
for i in range(9):
    total -= cands[i]
    for j in range(i+1, 9):
        total -= cands[j]
    
        if total == 100:
            del cands[j]
            del cands[i]
            found = True
            break
    
        total += cands[j]   
    if found:
        break
    else:
        total += cands[i]    
        
for i in sorted(cands):
    print(i)