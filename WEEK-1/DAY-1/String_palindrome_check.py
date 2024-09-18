def Is_palindrome_string(s):
    cleaned_string = s.replace(" ","").lower()

    reversed_string = cleaned_string[::-1]
    if reversed_string == cleaned_string:
        return "it is a palindrome"
    else:
        return "not a palindrome"
    

s = input("emter string")
        
result = Is_palindrome_string(s)
print(result)