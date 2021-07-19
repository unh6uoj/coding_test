def solution(nums):
    answer = 0

    nums.sort()

    cur_num = -1
    max_num = len(nums) / 2
    count = 0
    for num in nums:
        if num != cur_num:
            cur_num = num
            count += 1

        if count == max_num:
            break

    return count
