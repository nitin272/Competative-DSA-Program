from collections import defaultdict

def subarray_sum(nums, k):
    count = 0
    current_sum = 0
    sum_counts = defaultdict(int)
    sum_counts[0] = 1  

    for num in nums:
        current_sum += num
        count += sum_counts[current_sum - k]
        sum_counts[current_sum] += 1

    return count


nums = [1, 1, 1]
k = 2
print(subarray_sum(nums, k))  
