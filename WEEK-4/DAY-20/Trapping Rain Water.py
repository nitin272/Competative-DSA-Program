

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9


class Solution:
    def trap(self, height2):
        if not height:
            return 0
        
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        water_trapped = 0
        
       
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        
   
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        
   
        for i in range(n):
            water_trapped += min(left_max[i], right_max[i]) - height[i]
        
        return water_trapped

height = list(map(int, input("Enter heights separated by spaces: ").split()))
sol = Solution()
result = sol.trap(height)
print("Water trapped:", result)
