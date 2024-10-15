# Minimum Window Substring

from collections import Counter

def min_window(s, t):
    if not t or not s:  # Check if either string is empty
        return ""
    
    dict_t = Counter(t)  # Count characters in t
    required = len(dict_t)  # Number of unique characters in t
    l, r = 0, 0  # Initialize left and right pointers
    formed = 0  # Number of unique characters in the current window that match the requirement
    window_counts = {}  # Dictionary to keep counts of characters in the current window
    ans = float("inf"), None, None  # Tuple to store the smallest window (length, left, right)

    while r < len(s):  # Expand the window by moving right pointer
        character = s[r]  # Get the current character
        window_counts[character] = window_counts.get(character, 0) + 1  # Count the character

        if character in dict_t and window_counts[character] == dict_t[character]:  # Check if we have a valid character
            formed += 1  # Increment the formed count if we match a character requirement

        while l <= r and formed == required:  # Contract the window if all characters match
            character = s[l]  # Get the character at the left pointer

            # Update the smallest window if current is smaller
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            window_counts[character] -= 1  # Remove the leftmost character from the window
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1  # Decrement formed count if we lose a character match

            l += 1  # Move the left pointer to the right

        r += 1  # Move the right pointer to expand the window

    return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]  # Return the smallest window substring

# Example usage:
s = "ADOBECODEBANC"  # Change this string to test with different inputs
t = "ABC"  # Change this string to test with different inputs
result = min_window(s, t)
print(f"The minimum window substring of '{s}' containing all characters of '{t}' is: '{result}'")
