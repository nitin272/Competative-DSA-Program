# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return left


# nums = [1, 3, 5, 6]  # Example input to test the function
# target = 5

# Uncomment for user input
nums = list(map(int, input("Enter the sorted list of numbers (space-separated): ").split()))
target = int(input("Enter the target number: "))

solution = Solution()
result = solution.searchInsert(nums, target)

print(f"The target number should be inserted at index: {result}")
