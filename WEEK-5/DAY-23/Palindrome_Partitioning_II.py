class Solution(object):
    def minCut(self, s):
        length = len(s)
        palindrome_c = [-1] + [length] *length
        for i in range(2*length-1):
            R = i//2
            r = R + (i&1)
            while 0 <=R and r <length and s[R] == s[r]:
                palindrome_c[r+1] = min(palindrome_c[R+1], palindrome_c[R] +1)
                R -=1
                r -=1
        return     palindrome_c[-1]
     
# s = input("enter string")
s = "aab"

solution = Solution()
result = solution.minCut(s)
print(result)
