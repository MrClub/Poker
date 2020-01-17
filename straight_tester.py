# I want to figure out a way to detect straights

spam = [7, 6, 10, 10, 10, 10, 9]
ham = [3, 4, 5, 6, 7]

"""for e in ham:
    if e not in spam:
        print("not a straight")
    else:
        print("straight")"""


def straight_check(board_list):
    possible_straights = [
                          [10, 11, 12, 13, 1], [9, 10, 11, 12, 13], [8, 9, 10, 11, 12], [7, 8, 9, 10, 11],
                          [6, 7, 8, 9, 10], [5, 6, 7, 8, 9], [4, 5, 6, 7, 8], [3, 4, 5, 6, 7], [2, 3, 4, 5, 6],
                          [1, 2, 3, 4, 5]
                         ]

    for straight in possible_straights:
        count = 0
        for number in straight:
            if number in board_list:
                count += 1
            if count == 5:
                return True, straight
    return False, []


print(straight_check(spam))
