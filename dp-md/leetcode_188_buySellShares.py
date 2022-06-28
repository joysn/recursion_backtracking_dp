# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
# 188. Best Time to Buy and Sell Stock IV

# You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.
# Find the maximum profit you can achieve. You may complete at most k transactions.
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# Example 1:

# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
# Example 2:

# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. 
# Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

# Runtime: 582 ms, faster than 5.08% of Python3 online submissions for Best Time to Buy and Sell Stock IV.
# Memory Usage: 17.9 MB, less than 48.15% of Python3 online submissions for Best Time to Buy and Sell Stock IV.

def maxProfit(idx, buy, k):

    if idx == n:
        return 0

    if memo[idx][buy][k] != None:
        return memo[idx][buy][k]

    ans = maxProfit(idx+1,buy,k)
    if k == 0:
        return 0
    
    if buy:
        ans = max(ans,-prices[idx]+maxProfit(idx+1,False,k))
    else:
        ans = max(ans, prices[idx]+maxProfit(idx+1,True,k-1))
    memo[idx][buy][k] = ans
    return ans

if __name__ == "__main__":
    k = 2
    prices = [3,2,6,5,0,3]
    n = len(prices)
    memo = [[[None for i in range(k+1)] for j in range(2)] for x in range(n)]
    print(maxProfit(0,True, k))

    k = 2
    prices = [3,3,5,0,0,3,1,4]
    n = len(prices)
    memo = [[[None for i in range(k+1)] for j in range(2)] for x in range(n)]
    print(maxProfit(0,True, k))
    # print(memo)