# Factorial Calculation

def factorial(n):
    # Base case
    if n == 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

# Test input
print(factorial(5))  # Output should be 120
