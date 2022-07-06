# https://leetcode.com/problems/min-cost-climbing-stairs/
# 746. Min Cost Climbing Stairs

# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
# Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.
 

# Example 1:

# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.
# Example 2:

# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.

# Runtime: 85 ms, faster than 56.77% of Python3 online submissions for Min Cost Climbing Stairs.
# Memory Usage: 16.5 MB, less than 5.66% of Python3 online submissions for Min Cost Climbing Stairs.

class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        
        def minCost(idx):
            
            if idx >= n:
                return 0
            
            if idx in memo:
                return memo[idx]
            if idx + 1 < n:
                ans = min(cost[idx]+minCost(idx+1), cost[idx]+minCost(idx+2))
            else:
                ans = cost[idx]+minCost(idx+1)
            
            memo[idx] = ans
            return ans
        
        n = len(cost)
        memo = {}
        return min(minCost(0), minCost(1))



# Runtime: 93 ms, faster than 45.62% of Python3 online submissions for Min Cost Climbing Stairs.
# Memory Usage: 14.7 MB, less than 21.64% of Python3 online submissions for Min Cost Climbing Stairs.

class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        
        n = len(cost)
        dp = [0 for i in range(n)]
        
        dp[n-1] = cost[n-1] 
        dp[n-2] = cost[n-2]
        for i in range(n-3,-1,-1):
            dp[i] = min(dp[i+1]+cost[i], dp[i+2]+cost[i])
        
        return min(dp[0],dp[1])