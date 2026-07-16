def move_zero(nums):
    insert_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_index], nums[i] = nums[i], nums[insert_index]
            insert_index += 1
    return nums

print(move_zero([9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]))



# [0, 1, 0, 12, 3] -> [1, 12, 3, 0, 0]
# [0] -> [0]
# [1, 0, 13, 0, 0, 0, 5] -> [1, 13, 5, 0, 0, 0, 0]
# [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]
