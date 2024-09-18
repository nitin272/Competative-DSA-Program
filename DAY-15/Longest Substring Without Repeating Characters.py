# Given a string s, find the length of the longest substring without repeating characters.

# Input:
# The first line contains a string s.
# Output:
# Print the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length


# s = input("Enter a string: ")


s = "abcabcbb"

print(lengthOfLongestSubstring(s))

