# Given an array height representing the height of each vertical line, find two lines that together with the x-axis form a container, such that the container contains the most water.


# Input:
# 1 8 6 2 5 4 8 3 7

# Output:
# 49


def maxArea(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:
        width = right - left
        max_water = max(max_water, min(height[left], height[right]) * width)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water

height = list(map(int, input("Enter the heights (space-separated): ").split())) 

# height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))
