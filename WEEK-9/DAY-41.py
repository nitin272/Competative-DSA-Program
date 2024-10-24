def num_islands(grid):
    # Check if the grid is empty
    if not grid:
        return 0

    # Depth-first search function to mark the island as visited
    def dfs(i, j):
        # Check for out of bounds or if the cell is water ('0')
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return
        
        # Mark the land ('1') as visited by changing it to '0'
        grid[i][j] = '0'
        
        # Explore the neighboring cells (up, down, left, right)
        dfs(i + 1, j)  # Down
        dfs(i - 1, j)  # Up
        dfs(i, j + 1)  # Right
        dfs(i, j - 1)  # Left

    count = 0  # Initialize the count of islands
    # Iterate through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If a land cell ('1') is found, it indicates a new island
            if grid[i][j] == '1':
                dfs(i, j)  # Mark the entire island
                count += 1  # Increment the island count

    return count  # Return the total number of islands

# Default Input
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

# Run the function with the default input
result = num_islands(grid)
print(f"The number of islands is: {result}")
