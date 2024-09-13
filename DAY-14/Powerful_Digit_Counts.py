# Use print() to print to the console
def is_powerful(x, y):
    result = x ** y
    return len(str(result)) == y

n = int(input())

for i in range(1, 10):
    if is_powerful(i, n):
        print(i ** n)
