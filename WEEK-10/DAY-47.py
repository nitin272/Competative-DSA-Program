# Longest Consecutive Sequence

def longest_consecutive(nums):
    # Convert nums to a set for O(1) lookup
    num_set = set(nums)
    max_length = 0

    for num in num_set:
        # Check if it's the start of a sequence
        if num - 1 not in num_set:
            length = 1
            while num + length in num_set:
                length += 1
            max_length = max(max_length, length)

    return max_length

# Example input for testing
nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(nums))  # Output should be 4
