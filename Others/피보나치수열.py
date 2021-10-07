# 언휴는 이상한 꿈을 꾸었죠. 꿈 속에 요정이 나타나 다음과 같은 말을 했어요.
# “얘는 하루가 지나면 임신을 할 수 있어. 그리고 다음 날 부터 매일 한 마리씩 출산을 하지.
# 출산한 새끼들도 마찬가지야.”
# 꿈에서 깨었을 때 귀여운 생명체가 방에 있는 것을 알 수 있었죠.
# 요정의 말이 사실이라면 60일에는 몇 마리로 번식할 지 계산하고는 놀랐다고 하네요.(오늘을 1일이라고 가정)
# 언휴는 왜 놀랐는지 날짜 별로 개체 수를 확인하는 코드를 작성해 보세요.
# (*단 결과는 1초 이내에 나와야 합니다.)

# 입력은 일(기간)  , 출력은 개체 수
# 입력: 60
# 출력:1548008755920

# def breed(n):  # 재귀로 푸면 시간복잡도가 너무 크다 ..
#     if n < 3:
#         return 1
#     else:
#         return breed(n-1) + breed(n-2)


# print(breed(3))


# 동적 프로그래밍

heues = [0, 1, 1]


def dynamic_breed(n):
    if(n <= 0):
        return 0
    if(n < len(heues)):
        return heues[n]
    value = dynamic_breed(n-1)+dynamic_breed(n-2)
    heues.append(value)
    return value


for i in range(1, 12):
    print(dynamic_breed(i), end='\t')
print(dynamic_breed(60))
