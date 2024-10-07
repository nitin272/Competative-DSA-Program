def Count(nums):
    count =0
    def IsPrime(n):
        if n<=1:
            return False
        for i in range(2,int(n ** .5) +1):
            if n %i == 0:
                return False
        return True
    for num in nums:
        if IsPrime(num):
            count +=1
    return count
nums = list(map(int,input().split()))
print(Count(nums))
