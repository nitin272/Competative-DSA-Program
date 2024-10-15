# Count of Smaller Numbers After Self

def count_smaller(nums):
    sorted_list = []
    result = []

    for num in reversed(nums):
        index = binary_search(sorted_list, num)
        result.append(index)
        sorted_list.insert(index, num)

    return result[::-1]  # Reverse the result to match the original order

def binary_search(sorted_list, target):
    low, high = 0, len(sorted_list)
    while low < high:
        mid = (low + high) // 2
        if sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low

# Example usage
nums = [5, 2, 6, 1]
result = count_smaller(nums)
print(f"The count of smaller numbers after each element is: {result}")
