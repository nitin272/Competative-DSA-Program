# Top K Frequent Elements

from collections import Counter
import heapq

def top_k_frequent(nums, k):
    # Counter object to count frequencies
    freq_map = Counter(nums)
    # Use a heap to extract the k most common elements
    return [item for item, _ in heapq.nlargest(k, freq_map.items(), key=lambda x: x[1])]

# Example input for testing
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(top_k_frequent(nums, k))  # Output should be [1, 2]
