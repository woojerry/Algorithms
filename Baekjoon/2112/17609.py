# 12/31
# 17609 회문

T = int(input())
for _ in range(T):
    word = input()

    start, end = 0, len(word) - 1
    answer = 0
    palindrome = True
    pseudo_palindrome = True
    while start <= end:
        if word[start] == word[end]:
            start += 1
            end -= 1
        else:
            palindrome = False
            stop_start, stop_end = start, end
            answer = 2
            break

    if not palindrome:
       # print(word[start], word[end])
        if end - 1 != start and word[start] == word[end-1]:
            start += 1
            end -= 2
            answer = 1
            while start <= end:
                if word[start] == word[end]:
                    start += 1
                    end -= 1
                else:
                    pseudo_palindrome = False
                    answer = 2
                    break
        else:
            pseudo_palindrome = False

    if not pseudo_palindrome:
        start, end = stop_start, stop_end
        if start+1 != end and word[start + 1] == word[end]:
            start += 2
            end -= 1
            answer = 1
            while start <= end:
                if word[start] == word[end]:
                    start += 1
                    end -= 1
                else:
                    answer = 2
                    break

    #print(word[start], word[end])

    print(answer)
