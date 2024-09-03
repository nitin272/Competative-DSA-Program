class Solution(object):
    def getLucky(s, k):
        num =""
        for x in s:
            num += str(ord(x)- ord('a') +1)
        for _ in range(k):
            s =0
            for x in num:
                s += int(x)
            num = str(s)
        return int(num)
s = input("enter string")
k = int(input("enter K ifor the given string"))

solution= Solution()

result = Solution.getLucky(s,k)

print("the result is",result)