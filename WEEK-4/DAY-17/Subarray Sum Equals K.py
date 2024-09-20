# Given an array of integers and an integer k, find the total number of continuous subarrays whose sum equals k.


# Input:
# 1 1 1
# 2

# Output:
# 2


def subarraySum(nums: list[int], k: int) -> int:
    count = 0
    cumulative_sum = 0
    sum_counts = {0: 1}
    
    for num in nums:
        cumulative_sum += num
        if cumulative_sum - k in sum_counts:
            count += sum_counts[cumulative_sum - k]
        sum_counts[cumulative_sum] = sum_counts.get(cumulative_sum, 0) + 1
    
    return count


# nums = list(map(int, input("Enter the numbers (space-separated): ").split()))
# k = int(input("Enter the integer k: "))

# Hardcoded Input
nums = [1, 1, 1]
k = 2

print(subarraySum(nums, k))
