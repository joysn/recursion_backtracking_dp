# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# 122. Best Time to Buy and Sell Stock II
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.

# Example 2:
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.

# Example 3:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.


# Runtime: 121 ms, faster than 21.14% of Python3 online submissions for Best Time to Buy and Sell Stock II.
# Memory Usage: 15.5 MB, less than 7.49% of Python3 online submissions for Best Time to Buy and Sell Stock II.

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        
        def maxProfit(start):
            
            if start == n-1:
                return 0

            ib,i = start,start
            for i in range(ib+1,n):
                if prices[ib] >= prices[i]:
                    ib = i
                else:
                    break

            isell,i = ib,ib
            for i in range(isell+1,n):
                if prices[isell] < prices[i]:
                    isell = i
                else:
                    break
            return(prices[isell]-prices[ib] + maxProfit(isell))
                                

        return maxProfit(0)
        