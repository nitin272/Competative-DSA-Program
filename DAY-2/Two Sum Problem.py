def two_sum(nums, target):
    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    return []


nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Enter the target number: "))
result = two_sum(nums, target)
if result:
    print("Indices of the two numbers:", result)
else:
    print("No two numbers add up to the target.")
