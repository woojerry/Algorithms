def solution(tickets):
    # stack ver.
    dic = {}
    for st, ed in tickets:
        dic[st] = dic.get(st, []) + [ed]

    for key in dic.keys():  # dic의 값 리스트 값을 역순정렬
        dic[key].sort(reverse=True)  # stack을 사용할 것이므로 알파벳 역순으로 ,,

    answer = []
    stack = ["ICN"]
    while stack:
        print(answer)
        top = stack[-1]
        if top not in dic or len(dic[top]) == 0:  # dic에 없거나, 있어도 더이상 도착지가 없으면
            answer.append(stack.pop())  # path에 추가
        else:
            stack.append(dic[top].pop())  # stack에 추가

    return answer[::-1]


# global answer
# global dic
# answer = []
# dic = {}


# def dfs(city):
#     if city in dic:
#         while dic[city]:
#             dfs(dic[city].pop())

#     if city not in dic or len(dic[city]) == 0:
#         answer.append(city)
#         return


# def solution(tickets):
#     # recursion ver
#     for st, ed in tickets:
#         dic[st] = dic.get(st, []) + [ed]

#     for key in dic.keys():
#         dic[key].sort(reverse=True)
#     dfs("ICN")

#     return answer[::-1]

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], [
#       "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
