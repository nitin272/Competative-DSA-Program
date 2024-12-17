# Word Break 

# Function to determine if the string can be segmented
def wordBreak(s, wordDict):
    # Initialize a DP array with False values
    # dp[i] will be True if s[0:i] can be segmented into dictionary words
    dp = [False] * (len(s) + 1)
    dp[0] = True  # Base case: an empty string can be segmented
    
    # Convert wordDict to a set for faster lookup
    wordSet = set(wordDict)
    
    # Loop through each position in the string
    for i in range(1, len(s) + 1):
        # Check every possible split of s[0:i]
        for j in range(i):
            # If s[0:j] can be segmented and s[j:i] is in the dictionary
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break  # No need to check further if s[0:i] can already be segmented
    
    # The result is stored in the last element of the dp array
    return dp[len(s)]

# Example input for testing
s = "leetcode"
wordDict = ["leet", "code"]

# System input handling for dynamic input
if __name__ == "__main__":
    # Taking user input for testing
    s = input("Enter the string to check: ")
    wordDict = input("Enter the dictionary words (comma-separated): ").split(',')
    print("Can the string be segmented?", wordBreak(s, wordDict))
