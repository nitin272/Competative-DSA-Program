# Valid Parentheses

def is_valid(s):
    stack = []  # Initialize a stack to keep track of open brackets
    bracket_map = {')': '(', '}': '{', ']': '['}  # Map closing to opening brackets

    for char in s:  # Iterate through each character in the string
        if char in bracket_map:  # If the character is a closing bracket
            top_element = stack.pop() if stack else '#'  # Pop from stack or use dummy value
            if bracket_map[char] != top_element:  # Check if it matches the corresponding opening bracket
                return False  # Return false if it does not match
        else:
            stack.append(char)  # If it's an opening bracket, push it onto the stack

    return not stack  # Return True if stack is empty (all brackets matched)

# Example usage:
input_string = "{[()]}"  # Change this string to test with different inputs
result = is_valid(input_string)
print(f"The parentheses string '{input_string}' is valid: {result}")
