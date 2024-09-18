# Use print() to print to the console]
def sort_(nums):
  left,mid,right = 0,0,len(nums)-1
  while mid <=right:
    if nums[mid] ==0:
      nums[left],nums[mid] = nums[mid],nums[left]
      left +=1
      mid  +=1
    elif nums[mid] ==1:
      mid +=1
    else:
      nums[right],nums[mid] = nums[mid],nums[right]
      right -=1




size = input()
data = list(map(int,input().split()))
sort_(data)

print(*data)