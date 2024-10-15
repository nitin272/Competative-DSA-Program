# Unique Paths

def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]  # Initialize a 2D array with 1s

    for i in range(1, m):  # Start from the second row
        for j in range(1, n):  # Start from the second column
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]  # Number of paths to current cell

    return dp[-1][-1]  # Return the number of unique paths to the bottom-right corner

# Example usage:
m = 3  # Number of rows
n = 7  # Number of columns
result = unique_paths(m, n)
print(f"The number of unique paths in a {m}x{n} grid is: {result}")
