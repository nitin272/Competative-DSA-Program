# Given an array nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Input:
# 1 2 3 4

# Output:
# [24, 12, 8, 6]



def productExceptSelf(nums: list[int]) -> list[int]:
    output = [1] * len(nums)
    left_product = 1
    
    for i in range(len(nums)):
        output[i] = left_product
        left_product *= nums[i]
    
    right_product = 1
    for i in range(len(nums) - 1, -1, -1):
        output[i] *= right_product
        right_product *= nums[i]
    
    return output

# nums = list(map(int, input("Enter the numbers (space-separated): ").split()))
nums = [1, 2, 3, 4]

print(productExceptSelf(nums))
