
number = input()
length = len(number)
sum_of_digits = sum(int(d) for d in number)

if sum_of_digits == length * (length + 1) // 2:
    print('Yes')
else:
    print('No')
