# 12/27
# 3107

protocol = str(input())
answer = ''
if "::" in protocol:
    protocol = protocol.replace("::", ":*:")

groups = list(map(str, protocol.split(":")))

length = len(groups)
print(groups)
for group in groups:
    length -= 1

    if group == "*":
        for _ in range(9-len(groups)):  # "*" 의 공간 때문에 +1 해서 9
            answer += '0000:'

    else:
        if len(group) < 4:
            count = 4 - len(group)
            for _ in range(count):
                answer += '0'
            answer += group
        else:
            answer += group
        if length != 0:
            answer += ':'

print(answer)
