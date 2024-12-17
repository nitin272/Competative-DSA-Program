def length_of_longest_substring_two_distinct(s):
    from collections import defaultdict
    left, max_len = 0, 0
    char_map = defaultdict(int)  # To count occurrences of characters

    for right, char in enumerate(s):
        char_map[char] += 1  # Add the character at the right pointer
        # If more than 2 distinct characters, shrink the window from the left
        while len(char_map) > 2:
            char_map[s[left]] -= 1
            if char_map[s[left]] == 0:
                del char_map[s[left]]  # Remove the character from the map
            left += 1  # Slide the left pointer
        # Calculate the maximum length of the substring with at most 2 distinct chars
        max_len = max(max_len, right - left + 1)
    
    return max_len

# Hardcoded input for testing
s = "eceba"
print("Length of longest substring:", length_of_longest_substring_two_distinct(s))
