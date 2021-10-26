# isupper(), islower() 대문자, 소문자인지 확인해줌
def solution(word):
    frog_dict = {
        "A": "Z", "B": "Y", "C": "X", "D": "W", "E": "V", "F": "U", "G": "T", "H": "S", "I": "R", "J": "Q", "K": "P", "L": "O", "M": "N", "N": "M", "O": "L", "P": "K", "Q": "J", "R": "I", "S": "H", "T": "G", "U": "F", "V": "E", "W": "D", "X": "C,", "Y": "B", "Z": "A"
    }
    answer = ''
    for i in word:
        if i == " ":
            changed = ' '

        elif i.isupper() == True:
            changed = frog_dict[i]

        elif i.isupper() == False:
            tmp = i.upper()
            changed_upper = frog_dict[tmp]
            changed = changed_upper.lower()

        answer += changed

    return answer


print(solution('I love you'))
