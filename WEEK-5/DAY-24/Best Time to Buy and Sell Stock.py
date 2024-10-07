class Solution(object):
    def maxProfit(self, prices):
        min_prices = float('inf')
        Max_Profit = 0
        for price in prices:
            if price < min_prices:
                min_prices = price
            profit = price - min_prices

            if profit > Max_Profit:
                Max_Profit = profit
        return Max_Profit
    
prices = list(map(int,input("Emter number ").split()))
solution  = Solution()
print(solution.maxProfit(prices))
