
# Edit Distance (Levenshtein Distance)

def min_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:  # If first string is empty
                dp[i][j] = j  # Minimum operations = j (insert all characters from word2)
            elif j == 0:  # If second string is empty
                dp[i][j] = i  # Minimum operations = i (remove all characters from word1)
            elif word1[i - 1] == word2[j - 1]:  # Characters match
                dp[i][j] = dp[i - 1][j - 1]
            else:  # Perform insertion, deletion, or replacement
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])  # Min of insert, delete, or replace

    return dp[m][n]

# Hardcoded input for testing
word1 = "kitten"
word2 = "sitting"

print("Minimum edit distance:", min_distance(word1, word2))
