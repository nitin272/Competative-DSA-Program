# Given two Input numbers a and b representing a/b where a < b. Write a program to print all the reduced forms of the given fraction a/b in a single line. Print -1 if the Input is already in the most reduced fraction.

# Example:

# Input:  
# 6 12

# Output: 
# 3/6 2/4 1/2

# Explanation:
# 3/6, 2/4, and 1/2 are all the possible reduced forms of the given fraction which is 6/12.


def fraction(x, y):
    smaller = x if x < y else y
    flag = 1

    for i in range(2, smaller + 1):
        if x % i == 0 and y % i == 0:
            flag = 0
            print(str(x // i) + '/' + str(y // i), end=" ")

    if flag:
        print(-1)


# a, b = 4, 8  # Example input to test the function
a, b = map(int, input("Enter two numbers (space-separated): ").split())  # Uncomment for user input

if a < b:
    fraction(a, b)
