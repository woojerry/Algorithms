from collections import deque


def solution(record):
    answer = []

    sale = 0
    pre_buy = deque([])
    post_buy = []
    pre, post = 0, 0
    for i in record:
        action, price, count = i.split()
        if action == "P":
            pre_buy.append([int(price), int(count)])
            post_buy.append([int(price), int(count)])
        else:
            count = int(count)
            sale = int(count)

            while count > 0:
                recent_price, recent_count = post_buy.pop()
                if count > recent_count:
                    post += recent_price*(recent_count)
                    count -= recent_count
                else:
                    post += recent_price*count
                    if recent_count - count > 0:
                        rest = recent_count - count
                        post_buy.append([recent_price, rest])
                    count = 0

            while sale > 0:
                print(pre)
                re_price, re_count = pre_buy.popleft()
                if sale > re_count:
                    pre += re_price*(re_count)
                    sale -= re_count
                else:
                    pre += re_price*sale
                    if re_count - sale > 0:
                        re = re_count - sale
                        pre_buy.appendleft([re_price, re])
                    sale = 0

    answer.append(pre)
    answer.append(post)

    return answer


#print(solution(["P 300 6", "P 500 3", "S 1000 4", "P 600 2", "S 1200 1"]))

print(solution(	["P 100 4", "P 300 9", "S 1000 7",
      "P 1000 8", "S 700 7", "S 700 3"]))
