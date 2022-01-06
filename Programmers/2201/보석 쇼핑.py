# 투포인터

def solution(gems):
    cand = []
    kinds = len(set(gems))

    if kinds == 1:
        answer = [1, 1]
    else:
        dic = {}
        end = 0
        for start in range(0, len(gems)):
            while end < len(gems) and len(dic) != kinds:
                dic[gems[end]] = dic.get(gems[end], 0)+1
                end += 1

            if len(dic) == kinds:
                if len(cand) == 0:  # end 는 마지막에 +1 해줬으므로
                    cand.append(([start+1, end], end - start))
                else:  # 가장 짧은 구간 찾기
                    if cand[0][1] > end - start:
                        cand.pop()
                        cand.append(([start+1, end], end - start))

            if dic[gems[start]] > 1:
                dic[gems[start]] -= 1
            else:
                del dic[gems[start]]

        answer = cand[0][0]
    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA",
      "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
#print(solution(["AA", "AB", "AC", "AA", "AC"]))
