# Sudoku Solver

def solve_sudoku(board):
    def is_valid(board, row, col, num):
        # Check if the number is not in the current row, column, or 3x3 subgrid
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        return True

    def solve(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':  # If cell is empty
                    for num in '123456789':
                        if is_valid(board, row, col, num):
                            board[row][col] = num  # Try placing the number
                            if solve(board):  # Recurse
                                return True
                            board[row][col] = '.'  # Backtrack
                    return False  # No valid number found
        return True  # All cells are filled

    solve(board)

# Hardcoded input for testing (example of an unsolved Sudoku puzzle)
board = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9']
]

solve_sudoku(board)

# Output the solved Sudoku board
print("Solved Sudoku:")
for row in board:
    print(' '.join(row))
