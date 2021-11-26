# 11/26
# 1450 냅색문제
# MITM(Meet In The Middle) ?

def brute_force(start, end, item, total):
    if start >= len(item):
        total.append(end)
        return
    brute_force(start + 1, end, item, total)
    brute_force(start + 1, end + item[start], total)


N, C = map(int, input().split())
items = list(map(int, input().split()))

left, right = items[:N//2], items[N//2:]
left_sum, right_sum = [], []
