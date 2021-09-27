# 09/27
# 1157 단어 공부

word = input().upper()  # 입력 받으면서 대문자화
alphabets = set(word)  # 집합 자료형으로 바꿔 중복 제거
alphabets_list = list(alphabets)  # 다시 리스트로
counted_list = []  # 각 알파벳 count를 저장할 리스트

for i in alphabets_list:
    counted_list.append(word.count(i))  # 각 알파벳이 몇 개 있는지 센 뒤, 리스트에 저장

if(counted_list.count(max(counted_list)) > 1):  # 가장 많이 사용된 알파벳이 여러 개 존재하는 경우
    print('?')
else:
    # 가장 많이 사용된 알파벳의 인덱스 찾아서 원래 리스트에서 조회해 출력
    print(alphabets_list[counted_list.index(max(counted_list))])
