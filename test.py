people = [(21,'Junkyu'),(21,'Dohyun'),(20,'Sunyoung')]
print(sorted(people,key= lambda x: (-x[0],x[1]))) # 숫자는 내림차순으로
