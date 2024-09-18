def permute(nums):
    def backtrack(start):
        if start == len(nums):
            permutations.append(nums[:])
        else:
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

    permutations = []
    backtrack(0)
    return permutations

nums = list(map(int, input("Enter numbers separated by spaces: ").strip().split()))
result = permute(nums)
for perms in result:
    print(perms)
