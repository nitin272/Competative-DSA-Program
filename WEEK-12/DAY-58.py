# Trapping Rain Water


# Function to calculate the trapped rainwater
def trap_rain_water(heights):
    if not heights:
        return 0

    n = len(heights)
    left_max = [0] * n
    right_max = [0] * n

    # Fill left_max array
    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], heights[i])

    # Fill right_max array
    right_max[n - 1] = heights[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i])

    # Calculate trapped water
    trapped_water = 0
    for i in range(n):
        trapped_water += min(left_max[i], right_max[i]) - heights[i]

    return trapped_water


# Example input for testing
heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# heights = list(map(int, input("Enter the heights of the bars (comma-separated): ").split(',')))
print("Total water trapped:", trap_rain_water(heights))
