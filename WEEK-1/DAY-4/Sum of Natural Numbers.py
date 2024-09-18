def sum_of_natural_numbers_loop(n):
    return sum(range(1, n + 1))

def sum_of_natural_numbers_formula(n):
    return n * (n + 1) // 2

# Taking system input
n = int(input("Enter a number: "))
print("Sum using loop:", sum_of_natural_numbers_loop(n))
print("Sum using formula:", sum_of_natural_numbers_formula(n))
