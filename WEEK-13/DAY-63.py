# Longest Increasing Subsequence


def length_of_lis(nums):
    if not nums:
        return 0
    
    dp = [1] * len(nums)  # Initialize DP array, each element is an LIS of length 1
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)  # Update the length of the LIS ending at i
    
    return max(dp)  # Return the maximum length of LIS in the entire array

# Hardcoded input for testing
nums = [10, 9, 2, 5, 3, 7, 101, 18]

print("Length of Longest Increasing Subsequence:", length_of_lis(nums))
