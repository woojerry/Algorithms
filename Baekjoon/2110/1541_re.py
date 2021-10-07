# 10/06
# 1541 잃어버린 괄호

inputs = input().split("-")  # -로 짜르기

result = 0

for i in inputs[0].split("+"):
    result += int(i)


for i in inputs[1:]:
    for j in i.split("+"):
        result -= int(j)

print(result)
