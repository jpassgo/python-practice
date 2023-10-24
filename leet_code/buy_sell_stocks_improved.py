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
        max = 0
        min = prices[0]
        end = len(prices) - 1
        start = 0
        while end > start:
            if prices[start] < min:
                min = prices[start]
            if prices[end] > max:
                max = prices[end]

            start += 1
            end -= 1

        max_profit = max - min
        return max_profit if max_profit > 0 else 0


solution = Solution()

# No profits to be made
print(
    f"Profit to be made from stocks: \n Stocks: {[7,6,4,3,1]} \n Profit: ${solution.maxProfit([7,6,4,3,1])}"
)

# Max profit of 5
print(
    f"Profit to be made from stocks: \n Stocks: {[7,1,5,3,6,4]} \n Profit: ${solution.maxProfit([7,1,5,3,6,4])}"
)
