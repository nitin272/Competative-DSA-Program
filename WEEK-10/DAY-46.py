# Subarray Sum Equals K

def subarray_sum(nums, k):
    # HashMap to store cumulative sum and frequency
    cumulative_sum = 0
    count = 0
    sum_dict = {0: 1}  # Default cumulative sum to handle edge cases

    for num in nums:
        cumulative_sum += num
        # If cumulative_sum - k exists, it means we found a subarray with sum k
        if (cumulative_sum - k) in sum_dict:
            count += sum_dict[cumulative_sum - k]
        # Add the cumulative_sum to the hashmap
        sum_dict[cumulative_sum] = sum_dict.get(cumulative_sum, 0) + 1

    return count

# Example input for testing
nums = [1, 1, 1]
k = 2
print(subarray_sum(nums, k))  # Output should be 2
