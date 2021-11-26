def solution(ings, menu, sell):
    answer = 0
    ing_dict = {}
    benefit = {}

    for ing in ings:
        a, b = ing.split()
        ing_dict[a] = int(b)

    for food in menu:
        name, ingr, price = food.split()
        tmp = 0
        for j in ingr:
            tmp += ing_dict[j]
        benefit[name] = int(price) - tmp

    for k in sell:
        c, d = k.split()
        answer += benefit[c] * int(d)

    return answer


print(solution(["r 10", "a 23", "t 124", "k 9"], ["PIZZA arraak 145", "HAMBURGER tkar 180",
      "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45", "JUICE rra 55", "WATER a 20"], ["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]))
