def maximumSubarraySum(arr):
    n = len(arr)
    maxSum = float('-inf')
    currSum = 0

    for i in range(n):
        currSum += arr[i]
        maxSum = max(maxSum, currSum)
        if currSum < 0:
            currSum = 0

    return maxSum


# N = int(input("Enter the number of elements: "))
# arr = list(map(int, input("Enter the elements: ").split()))[:N]


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_sum = maximumSubarraySum(arr)
print("Maximum Subarray Sum:", 0 if max_sum == float('-inf') else max_sum)

