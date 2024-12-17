# Sliding Window Maximum

from collections import deque

def maxSlidingWindow(nums, k):
    result = []
    dq = deque()  # Deque to store indices of elements in the current window
    
    for i, num in enumerate(nums):
        # Remove indices that are out of the current window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove indices of elements smaller than the current element
        while dq and nums[dq[-1]] < num:
            dq.pop()
        
        dq.append(i)
        
        # Add the maximum value (first element in the deque) when the window is fully formed
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

# Example input for testing
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3


nums = list(map(int, input("Enter the list of numbers (comma-separated): ").split(',')))
k = int(input("Enter the window size (k): "))
print("Maximums in sliding window:", maxSlidingWindow(nums, k))
