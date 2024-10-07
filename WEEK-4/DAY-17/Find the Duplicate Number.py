# Given an array of n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Find the duplicate number.

# Input:
# 1 3 4 2 2

# Output:
# 2


def findDuplicate(nums: list[int]) -> int:
    slow = nums[0]
    fast = nums[0]
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow

# nums = list(map(int, input("Enter the numbers (space-separated): ").split()))
nums = [1 ,3 ,4 ,2, 2]
print(findDuplicate(nums))
