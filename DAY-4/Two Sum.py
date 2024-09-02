def two_sum_bruteforce(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def two_sum_hashmap(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

# Taking system input
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Enter the target sum: "))
print("Indices using brute-force:", two_sum_bruteforce(nums, target))
print("Indices using hash map:", two_sum_hashmap(nums, target))
