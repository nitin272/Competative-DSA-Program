def find_median_sorted_arrays(nums1, nums2):
    # Ensure nums1 is the smaller array for binary search optimization
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    x, y = len(nums1), len(nums2)

    low, high = 0, x  # Binary search on the smaller array
    while low <= high:
        partition_x = (low + high) // 2
        partition_y = (x + y + 1) // 2 - partition_x

        # Handle edge cases when partitioning the arrays
        max_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
        min_x = float('inf') if partition_x == x else nums1[partition_x]
        max_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
        min_y = float('inf') if partition_y == y else nums2[partition_y]

        # Check if we have a valid partition
        if max_x <= min_y and max_y <= min_x:
            if (x + y) % 2 == 0:
                # If total length is even, take the average of two middle numbers
                return (max(max_x, max_y) + min(min_x, min_y)) / 2
            else:
                # If total length is odd, take the maximum of the left half
                return max(max_x, max_y)
        elif max_x > min_y:
            high = partition_x - 1  # Move left
        else:
            low = partition_x + 1  # Move right

    raise ValueError("Input arrays are not sorted.")

# Hardcoded input for testing
nums1 = [1, 3]
nums2 = [2]
print("Median:", find_median_sorted_arrays(nums1, nums2))
