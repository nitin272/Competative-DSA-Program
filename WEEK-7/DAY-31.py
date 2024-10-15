#  Longest Palindromic Substring

def longest_palindrome(s):
    def expand_around_center(left: int, right: int) -> str:
        # Expand while the characters at both ends are the same
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1  # Move left pointer inward
            right += 1  # Move right pointer inward
        return s[left + 1:right]  # Return the palindromic substring

    longest = ""  # Initialize the longest palindromic substring
    for i in range(len(s)):  # Iterate through each character in the string
        # Odd-length palindromes (single character center)
        odd_palindrome = expand_around_center(i, i)
        # Even-length palindromes (two identical characters center)
        even_palindrome = expand_around_center(i, i + 1)
        
        # Update the longest palindrome found
        longest = max(longest, odd_palindrome, even_palindrome, key=len)

    return longest  # Return the longest palindromic substring

# Example usage:
input_string = "babad"  # Change this string to test with different inputs
result = longest_palindrome(input_string)
print(f"The longest palindromic substring is: '{result}'")
