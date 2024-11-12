# Product of Array Except Self

def product_except_self(nums):
    length = len(nums)
    result = [1] * length

    # Calculate left products
    left_product = 1
    for i in range(length):
        result[i] = left_product
        left_product *= nums[i]

    # Calculate right products and combine with left products
    right_product = 1
    for i in range(length - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result

# Example input for testing
nums = [1, 2, 3, 4]
print(product_except_self(nums))  # Output should be [24, 12, 8, 6]
