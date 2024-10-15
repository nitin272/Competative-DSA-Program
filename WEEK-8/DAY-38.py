# N-Queens

def solve_n_queens(n):
    def is_not_under_attack(row, col):
        return col not in cols and (row - col) not in diag1 and (row + col) not in diag2

    def place_queen(row, col):
        queens.add((row, col))
        cols.add(col)
        diag1.add(row - col)
        diag2.add(row + col)

    def remove_queen(row, col):
        queens.remove((row, col))
        cols.remove(col)
        diag1.remove(row - col)
        diag2.remove(row + col)

    def backtrack(row=0):
        if row == n:
            output.append(['.' * col + 'Q' + '.' * (n - col - 1) for row, col in queens])
            return
        for col in range(n):
            if is_not_under_attack(row, col):
                place_queen(row, col)
                backtrack(row + 1)
                remove_queen(row, col)

    output = []
    queens = set()
    cols = set()
    diag1 = set()
    diag2 = set()
    backtrack()
    return output

# Example usage
n = 4
result = solve_n_queens(n)
print("The solutions for the N-Queens problem are:")
for solution in result:
    for row in solution:
        print(row)
    print()
