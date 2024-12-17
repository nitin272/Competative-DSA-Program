# Longest Substring Without Repeating Characters

def lengthOfLongestSubstring(s):
    # Dictionary to store the last occurrence index of characters
    char_map = {}
    left = 0  # Left pointer of the sliding window
    max_len = 0  # Result variable to store the maximum length
    
    # Iterate through the string
    for right in range(len(s)):
        # If the character is already in the window, move the left pointer
        if s[right] in char_map and char_map[s[right]] >= left:
            left = char_map[s[right]] + 1
        
        # Update the last occurrence index of the character
        char_map[s[right]] = right
        
        # Update the maximum length of the substring
        max_len = max(max_len, right - left + 1)
    
    return max_len

# Example input for testing
s = "abcabcbb"

# System input handling for dynamic input
if __name__ == "__main__":
    s = input("Enter the string: ")
    print("Length of the longest substring without repeating characters:", lengthOfLongestSubstring(s))
