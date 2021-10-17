# 10/17

def solution(numbers, hand):
    answer = ''
    location = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (
        2, 0), 8: (2, 1), 9: (2, 2), '*': (3, 0), 0: (3, 1), '#': (3, 2)}

    left_hand, right_hand = '*', '#'

    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            left_hand = num
            continue
        elif num in [3, 6, 9]:
            answer += 'R'
            right_hand = num
            continue
        else:  # 2,5,8,0
            d_L = abs(location[num][0] - location[left_hand][0]) + \
                abs(location[num][1] - location[left_hand][1])
            d_R = abs(location[num][0] - location[right_hand][0]) + \
                abs(location[num][1] - location[right_hand][1])
            if d_L > d_R:
                answer += 'R'
                right_hand = num
            elif d_L < d_R:
                answer += 'L'
                left_hand = num
            elif d_L == d_R:
                if hand == 'right':
                    answer += 'R'
                    right_hand = num
                else:
                    answer += 'L'
                    left_hand = num
    return answer
