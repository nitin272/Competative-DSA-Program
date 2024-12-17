# Decode Ways

def numDecodings(s):
    # Base case: empty string has one way to decode
    if not s:
        return 0
    
    # dp[i] will store the number of ways to decode s[:i]
    dp = [0] * (len(s) + 1)
    dp[0] = 1  # There's one way to decode an empty string
    
    for i in range(1, len(s) + 1):
        # If the current digit is valid, decode it
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]
        
        # If the last two digits form a valid two-digit number, decode it
        if i > 1 and '10' <= s[i - 2:i] <= '26':
            dp[i] += dp[i - 2]
    
    return dp[len(s)]

# Example input for testing
s = "226"

# System input handling for dynamic input
if __name__ == "__main__":
    s = input("Enter the encoded string: ")
    print("Number of ways to decode:", numDecodings(s))
