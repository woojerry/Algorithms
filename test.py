def palindrome(words):
    is_palindrome = True
    for i in range(len(words) // 2):
        if words[i] != words[-1 - i]:      #
            is_palindrome = False        # 회문이 아님
            break
    # print(words)

    return is_palindrome


print(palindrome('abc'))
