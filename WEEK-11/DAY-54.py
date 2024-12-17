# Combination Sum

def combinationSum(candidates, target):
    result = []
    
    def backtrack(start, target, current_combination):
        if target == 0:
            result.append(list(current_combination))
            return
        if target < 0:
            return
        
        for i in range(start, len(candidates)):
            current_combination.append(candidates[i])
            backtrack(i, target - candidates[i], current_combination)
            current_combination.pop()
    
    backtrack(0, target, [])
    return result

# Example input for testing
candidates = [2, 3, 6, 7]
target = 7

# System input handling for dynamic input
if __name__ == "__main__":
    candidates = list(map(int, input("Enter the candidates (comma-separated): ").split(',')))
    target = int(input("Enter the target value: "))
    print("Combinations that sum to target:", combinationSum(candidates, target))
