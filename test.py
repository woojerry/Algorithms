def solution(n, jump):
    arr = [[0] * n for _ in range(n)]  # 1
    row = 0  # 2
    col = 0  # 2
    cnt = 1  # 3
    trans = 1  # 4
    arr[0][0] = 1
    number = 1
    while number > (n*n):
        col_size, row_size = n
        # for i in range(n):  # 6
        # 가로 이동
        # while col < n:
        while True:
            col += (jump-1)
            if col > col_size:
                col = n-1
                col_size -= 1
                break
            else:
                number += 1
                arr[row][col] = cnt

        # n -= 1  # 7
        for j in range(n):  # 8
            row += trans
            arr[row][col] = cnt
            cnt += 1
        trans *= -1  # 9
    print(arr)
    return arr


print(snail(5))
