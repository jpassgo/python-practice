# 
# 121. Best Time to Buy and Sell Stock
# 
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# 
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        i = len(prices) - 1
        while i > 0:
            for j in range(i - 1):
                profit = prices[i] - prices[j]
                if profit > 0:
                    profits.append(profit)
            i -= 1

        
        return max(profits) if len(profits) > 0 else 0


    
solution = Solution()

# No profits to be made
print(f'Profit to be made from stocks: \n Stocks: {[7,6,4,3,1]} \n Profit: ${solution.maxProfit([7,6,4,3,1])}')

# Max profit of 5
print(f'Profit to be made from stocks: \n Stocks: {[7,1,5,3,6,4]} \n Profit: ${solution.maxProfit([7,1,5,3,6,4])}')