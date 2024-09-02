def find_missing_number(nums):
    n = len(nums) + 1
    total_sum = n * (n + 1) 
    actual_sum = sum(nums)
    return total_sum - actual_sum

nums = list(map(int, input("Enter the numbers separated by spaces: ").split()))
print("Missing number:", find_missing_number(nums))
