class Solution:
    def sortColors(self, nums):
        l,r = 0 ,len(nums)-1
        i = 0


        def swap(i,j):
            temp  = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
    
        while i <=r:
            if nums[i]==0:
                swap(l,i)
                l+=1
            elif nums[i] ==2:
                swap(i,r)
                r-=1
                i -=1
            i+=1
        return nums
    
nums  = list(map(int,input("enter nums").split()))
solution  = Solution()
print(solution.sortColors(nums))





# class Solution:
#     def sortColors(self, nums):
#         low, mid, high = 0, 0, len(nums) - 1
        
#         while mid <= high:
#             if nums[mid] == 0:  # Red (0)
#                 nums[low], nums[mid] = nums[mid], nums[low]
#                 low += 1
#                 mid += 1
#             elif nums[mid] == 1:  # White (1)
#                 mid += 1
#             else:  # Blue (2)
#                 nums[mid], nums[high] = nums[high], nums[mid]
#                 high -= 1
