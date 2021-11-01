def solution(board):
    answer = 0

    return answer


# [[1, -7, -2, 1, -1],[2, 3, 0, -1, -2],[1, -1, 6, -1, -2],[-1, 1, -2, 0, 4],[-10, 5, -3, -1, 1]] / 18
# [[-10, 20, 30],[-10, 0, 10],[-20, 40, 1]] / 61


# from pprint import pprint
# 경계 0처리 아직 안함

# def solution(arr):
#     size = len(arr)
#     dp = [[[0, 0] for __ in range(size)] for _ in range(size)]
#     dp[0][0][0], dp[0][0][1] = arr[0][0], arr[0][0]

#     for i in range(1, size):
#         dp[0][i][0] = dp[0][i - 1][0] + arr[0][i]
#         dp[0][i][1] = dp[0][i - 1][1] + arr[0][i]
#         dp[i][0][0] = dp[i - 1][0][0] + arr[i][0]
#         dp[i][0][1] = dp[i - 1][0][1] + arr[i][0]

#     for r in range(1, size):
#         for c in range(1, size):
#             dp[r][c][0] = max(dp[r - 1][c][0] + arr[r][c], dp[r][c - 1][0] + arr[r][c])
#             dp[r][c][1] = min(dp[r - 1][c][1] + arr[r][c], dp[r][c - 1][1] + arr[r][c])

#             if arr[r][c] == 0:
#                 dp[r][c][0] = max(-dp[r][c][1], dp[r][c][0])
#                 dp[r][c][1] = min(-dp[r][c][0], dp[r][c][-1])

#     return max(dp[size - 1][size - 1])


# print(
#     solution(
#         [
#             [1, -7, -2, 1, -1],
#             [2, 3, 0, -1, -2],
#             [1, -1, 6, -1, -2],
#             [-1, 1, -2, 0, 4],
#             [-10, 5, -3, -1, 1],
#         ]
#     )
# )
# print(solution([[-10, 20, 30], [-10, 0, 10], [-20, 40, 1]]))
