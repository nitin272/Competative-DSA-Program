def min_path_sum(grid):
    if not grid:
        return 0
    
    m, n = len(grid), len(grid[0])
    
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            top = grid[i - 1][j] if i > 0 else float('inf')
            left = grid[i][j - 1] if j > 0 else float('inf')
            grid[i][j] += min(top, left)

    return grid[m - 1][n - 1]

# Example usage
grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(min_path_sum(grid))  # Output: 7
