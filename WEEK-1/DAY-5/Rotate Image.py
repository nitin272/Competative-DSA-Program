def rotate(matrix):
    n = len(matrix)
  
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
  
    for row in matrix:
        row.reverse()


n = int(input("Enter the size of the matrix (n x n): "))
matrix = []
print("Enter the matrix rows:")
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
rotate(matrix)
print("Rotated matrix:")
for row in matrix:
    print(" ".join(map(str, row)))
