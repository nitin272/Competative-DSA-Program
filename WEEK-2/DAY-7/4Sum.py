# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]


from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                start, end = j + 1, n - 1
                while start < end:
                    sum_ = nums[i] + nums[j] + nums[start] + nums[end]

                    if sum_ == target:
                        ans.append([nums[i], nums[j], nums[start], nums[end]])
                        start += 1
                        end -= 1

                        while start < end and nums[start] == nums[start - 1]:
                            start += 1
                        while start < end and nums[end] == nums[end + 1]:
                            end -= 1
                    elif sum_ > target:
                        end -= 1
                    else:
                        start += 1

        return ans


nums = list(map(int, input("Enter the elements separated by spaces: ").split()))
target = int(input("Enter the target: "))

solution = Solution()
result = solution.fourSum(nums, target)
    
if result:
    print("Quadruplets that sum to the target:")
    for quad in result:
        print(quad)
else:
    print("No quadruplets found that sum to the target.")
