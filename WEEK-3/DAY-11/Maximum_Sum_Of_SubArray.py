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

N = int(input(""))
arr = list(map(int, input("").split()))[:N]
max_sum = maximumSubarraySum(arr)

print("", 0 if max_sum == float('-inf') else max_sum)
