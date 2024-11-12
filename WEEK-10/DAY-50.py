# Coin Change

def coin_change(coins, amount):
    # Initialize dp array with amount+1 as a placeholder for infinity
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

# Example input for testing
coins = [1, 2, 5]
amount = 11
print(coin_change(coins, amount))  # Output should be 3
