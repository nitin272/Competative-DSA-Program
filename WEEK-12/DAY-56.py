# Largest Rectangle in Histogram

def largestRectangleArea(heights):
    stack = []
    max_area = 0
    
    for i, height in enumerate(heights):
        # Calculate area for each bar and pop from stack
        while stack and heights[stack[-1]] > height:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    
    # Calculate area for remaining bars
    while stack:
        h = heights[stack.pop()]
        w = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, h * w)
    
    return max_area

# Example input for testing
heights = [2, 1, 5, 6, 2, 3]

# System input handling for dynamic input
if __name__ == "__main__":
    heights = list(map(int, input("Enter the heights of the bars (comma-separated): ").split(',')))
    print("Maximum area of rectangle:", largestRectangleArea(heights))
