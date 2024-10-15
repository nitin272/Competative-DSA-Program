def rotate(nums, k):
    n = len(nums)
    k = k % n 
    nums[:] = nums[-k:] + nums[:-k]


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]
