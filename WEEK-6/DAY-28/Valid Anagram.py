def is_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

# Example usage
s = "anagram"
t = "nagaram"
print(is_anagram(s, t))  # Output: True
