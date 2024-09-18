def Fizz_buzz(n):
    if 0 < n <= 100:
        for i in range(1,n+1):
            if i%3 ==0 and i % 5 ==0:
                print("Fizzbuzz",end=" ")
            elif i%3 ==0:
                print("Fizz",end=" ")
            elif i % 5 ==0:
                print("Buzz",end = " ")
            else:
                print(i,end = " ")
    else:
        print(-1)

n =int(input("enter number"))

Fizz_buzz(n)

