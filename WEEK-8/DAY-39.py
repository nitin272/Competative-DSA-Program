# Word Search II


def find_words(board, words):
    from collections import defaultdict, deque

    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_end_of_word = False

    class Trie:
        def __init__(self):
            self.root = TrieNode()

        def insert(self, word):
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end_of_word = True

    def backtrack(r, c, node, path):
        letter = board[r][c]
        curr_node = node.children[letter]
        if curr_node.is_end_of_word:
            result.add(path)
            curr_node.is_end_of_word = False  # Avoid duplicate entries
        board[r][c] = "#"  # Mark the cell as visited
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] in curr_node.children:
                backtrack(nr, nc, curr_node, path + board[nr][nc])
        board[r][c] = letter  # Restore the cell

    trie = Trie()
    for word in words:
        trie.insert(word)

    result = set()
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] in trie.root.children:
                backtrack(r, c, trie.root, board[r][c])

    return list(result)

# Example usage
board = [["o", "a", "a", "n"],
         ["e", "t", "a", "e"],
         ["i", "h", "k", "r"],
         ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain"]
result = find_words(board, words)
print(f"The words found in the board are: {result}")
