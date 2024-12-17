#  Find the largest square submatrix of 1's in a binary matrix.

def maximal_square(matrix):
    if not matrix:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]  # DP table to store the largest square's side length ending at (i, j)
    max_side = 0  # To track the maximum side length of the square found

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':  # Only consider cells with '1'
                if i == 0 or j == 0:  # First row or first column
                    dp[i][j] = 1  # The largest square ending at this cell is 1 (just the cell itself)
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1  # Take the min of the three neighbors + 1
                max_side = max(max_side, dp[i][j])  # Update the maximum side length of the square found

    return max_side * max_side  # Area of the largest square

# Hardcoded input for testing
matrix = [
    ['1', '0', '1', '0', '0'],
    ['1', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1'],
    ['1', '0', '0', '1', '0']
]

print("Largest square area of 1's:", maximal_square(matrix))
