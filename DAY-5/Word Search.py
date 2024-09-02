def exist(board, word):
    def dfs(i, j, word_index):
        if word_index == len(word):
            return True
        if (i < 0 or i >= len(board) or j < 0 or j >= len(board) or 
            board[i][j] != word[word_index]):
            return False
        
        temp, board[i][j] = board[i][j], '#'
        found = (dfs(i + 1, j, word_index + 1) or 
                 dfs(i - 1, j, word_index + 1) or 
                 dfs(i, j + 1, word_index + 1) or 
                 dfs(i, j - 1, word_index + 1))
        board[i][j] = temp
        return found

    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, 0):
                return True
    return False


m = int(input("Enter the number of rows in the board: "))
n = int(input("Enter the number of columns in the board: "))
print("Enter the board rows:")
board = [list(input().strip()) for _ in range(m)]
word = input("Enter the word to search: ")
print("Word exists in the board:" if exist(board, word) else "Word does not exist in the board.")
