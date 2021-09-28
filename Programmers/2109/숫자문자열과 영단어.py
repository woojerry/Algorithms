def solution(s):  # s가 의미하는 원래 숫자를 return 하는 함수

    english = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
               'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    englist_keys = list(english.keys())  # key값들을 리스트로 만들기

    for i in englist_keys:
        if i in s:
            s = s.replace(i, english[i])

    answer = int(s)
    return answer
