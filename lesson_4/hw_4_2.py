def calculate_even_sum(nums):
    if not nums:
        return 0
    return sum(nums[0::2]) * nums[-1]

print(calculate_even_sum([]))


# [1, 3, 5] => 30
# [6] => 36
# [] => 0
