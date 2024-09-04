def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def print_fibonacci(n):
    for i in range(n+1):
        print(fibonacci(i), end=' ')


n = int(input())
print_fibonacci(n)