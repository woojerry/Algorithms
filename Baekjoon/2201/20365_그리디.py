# 01/11
# 20365 블로그2
# 그리디

N = int(input())
colors = input()
prev = colors[0]
blue = 0
red = 0

if prev == "R":
    red += 1
else:
    blue += 1

for color in colors:
    if color != prev:
        if color == "B":
            blue += 1
            prev = "B"
        else:
            red += 1
            prev = "R"

print(1 + min(blue, red))  # 연속된 거 그룹수 적은거로
