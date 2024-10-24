def product_except_self(nums):
    # Get the length of the input list
    length = len(nums)
    # Initialize the output list with 1s
    output = [1] * length

    # Calculate left products
    left_product = 1  # This will hold the product of all elements to the left of the current index
    for i in range(length):
        output[i] = left_product  # Set the output at the current index to the left product
        left_product *= nums[i]    # Update the left product for the next index

    # Calculate right products
    right_product = 1  # This will hold the product of all elements to the right of the current index
    for i in range(length - 1, -1, -1):
        output[i] *= right_product  # Multiply the output at the current index by the right product
        right_product *= nums[i]     # Update the right product for the next index

    return output  # Return the final output list

# Default Input
nums = [1, 2, 3, 4]
# Run the function with the default input
result = product_except_self(nums)
print(f"Product of array except self: {result}")
