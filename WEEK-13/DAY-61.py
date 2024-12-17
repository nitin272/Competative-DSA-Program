# Minimum Window Substring

def min_window(s, t):
    from collections import Counter
    if not t or not s:
        return ""

    t_count = Counter(t)  # Count of characters in t
    current_count = Counter()  # Count of characters in the current window
    start, end = 0, float('inf')  # Start and end indices of the minimum window
    l = 0  # Left pointer for the sliding window

    for r in range(len(s)):  # Right pointer expands the window
        current_count[s[r]] += 1
        # Check if the current window contains all characters of t
        while all(current_count[char] >= t_count[char] for char in t_count):
            # Update the smallest window if found
            if r - l < end - start:
                start, end = l, r
            current_count[s[l]] -= 1  # Shrink the window from the left
            l += 1

    return s[start:end + 1] if end != float('inf') else ""

# Hardcoded input for testing
s = "ADOBECODEBANC"
t = "ABC"
print("Minimum window substring:", min_window(s, t))
