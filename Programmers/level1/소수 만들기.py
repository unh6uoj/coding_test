from itertools import permutations


def solution(nums):
    answer = 0

    temp = list([sum(i) for i in list(permutations(nums, 3))])
    for i in temp:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            answer += 1

    return answer/6
