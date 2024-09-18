def is_palindrome(n):
    original = n
    reversed_num = 0
    
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
    
    return original == reversed_num


number = int(input().replace(" ",""))
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
