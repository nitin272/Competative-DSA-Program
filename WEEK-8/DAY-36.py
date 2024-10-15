#  Longest Valid Parentheses

def longest_valid_parentheses(s):
    max_length = 0
    stack = [-1]

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])

    return max_length

# Example usage
s = "(()())"
result = longest_valid_parentheses(s)
print(f"The length of the longest valid parentheses substring is: {result}")
