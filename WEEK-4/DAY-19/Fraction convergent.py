# Input:  
# 16 10

# Output:  
# 8 5

# Explanation: 
# The lowest fraction that 16/10 can be reduced to is 8/5 and hence 8 5 is the desired output.






def gcd(x, y):
    smaller = y if x > y else x
    for i in range(1, smaller + 1):
        if x % i == 0 and y % i == 0:
            hcf = i 
    return hcf

a, b = map(int, input().split())
div = gcd(a, b)
print(a // div, b // div)
