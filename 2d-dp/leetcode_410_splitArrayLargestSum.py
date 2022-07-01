# https://leetcode.com/problems/split-array-largest-sum/
# 410. Split Array Largest Sum

# Given an array nums which consists of non-negative integers and an integer m, 
# you can split the array into m non-empty continuous subarrays.

# Write an algorithm to minimize the largest sum among these m subarrays.

 

# Example 1:
# Input: nums = [7,2,5,10,8], m = 2
# Output: 18
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.

# Example 2:
# Input: nums = [1,2,3,4,5], m = 2
# Output: 9

# Example 3:
# Input: nums = [1,4,4], m = 3
# Output: 4

import sys
def maxSumSubArry(idx, curr_m):

    # base case
    if curr_m == 1:
        return sum(nums[idx:])
    
    # recursive case
    if memo[idx][curr_m] != -1:
        return memo[idx][curr_m]
    min_sum = sys.maxsize
    for pidx in range(idx,n-curr_m+1):
        max_sum = max(sum(nums[idx:pidx+1]),maxSumSubArry(pidx+1,curr_m-1))
        min_sum = min(min_sum,max_sum)
    memo[idx][curr_m] = min_sum
    return min_sum

if __name__=="__main__":
    nums = [7,2,5,10,8]
    m = 2
    n = len(nums)
    memo = [[-1 for i in range(m+1)] for j in range(n)]
    print("Top Down",maxSumSubArry(0,m))

    nums = [1,2,3,4,5]
    m = 2
    n = len(nums)
    memo = [[-1 for i in range(m+1)] for j in range(n)]
    print("Top Down",maxSumSubArry(0,m))


    nums = [1,4,4]
    m = 3
    n = len(nums)
    memo = [[-1 for i in range(m+1)] for j in range(n)]
    print("Top Down",maxSumSubArry(0,m))
