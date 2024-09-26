# p = int(input())
p = 12
flag = False

for a in range(1, p // 2):
    for b in range(1, p // 3):
        c = p - a - b
        if a + b > c and a + c > b and b + c > a:
            if a**2 + b**2 == c**2:
                flag = True
                break

if flag:
    print("Yes")
else:
    print("No")
