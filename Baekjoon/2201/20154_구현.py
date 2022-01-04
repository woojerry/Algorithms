# 1/3
# 20154 이 구역의 승자는 누구야?
alphabets = {
    'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 3, 'F': 3, 'G': 3, "H": 3, 'I': 1, 'J': 1, "K": 3, "L": 1, "M": 3, "N": 3, "O": 1, "P": 2, "Q": 2, "R": 2, "S": 1, "T": 2, "U": 1, "V": 1, 'W': 2, "X": 2, "Y": 2, "Z": 1
}

S = input()
#length = len(S)
sums = 0
for al in S:
    sums += alphabets[al]
    if sums >= 10:
        sums = sums % 10

if sums % 2 == 0:
    print("You're the winner?")
else:
    print("I'm a winner!")
