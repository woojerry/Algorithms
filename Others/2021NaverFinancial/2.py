def solution(n, jump):
    arr = [[0] * n for _ in range(n)]  # 1
    row = 0  # 2
    col = 0  # 2
    cnt = 1  # 3
    trans = 1  # 4
    arr[0][0] = 1
    number = 1
    sign = 1
    while True:
        col_size, row_size = n, n
        # for i in range(n):  # 6
        # 가로 이동
        # while col < n:
        while True:
            col += sign * (jump-1)
            if col > col_size:
                col = col_size-1
                col_size -= 1
                row_size -= 1
                break
                
            else:
                number += 1
                arr[row][col] = number

        if number == (n*n):
            break

        while True:
            row += sign * (jump - 1)
            if row > row_size:
                row = row_size - 1
                break
            else:
                number += 1
                arr[row][col] = number

        if number == (n*n):
            break

        sign *= -1  # 9
    print(arr)
    return arr


print(solution(5, 3))
