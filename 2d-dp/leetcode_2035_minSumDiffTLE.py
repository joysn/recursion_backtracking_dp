# 2035. Partition Array Into Two Arrays to Minimize Sum Difference
# https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/

# You are given an integer array nums of 2 * n integers. You need to partition nums into two arrays of length n to minimize 
# the absolute difference of the sums of the arrays. To partition nums, put each element of nums into one of the two arrays.

# Return the minimum possible absolute difference.

# Input: nums = [3,9,7,3]
# Output: 2
# Explanation: One optimal partition is: [3,9] and [7,3].
# The absolute difference between the sums of the arrays is abs((3 + 9) - (7 + 3)) = 2.


# Input: nums = [-36,36]
# Output: 72
# Explanation: One optimal partition is: [-36] and [36].
# The absolute difference between the sums of the arrays is abs((-36) - (36)) = 72.


# Input: nums = [2,-1,0,4,-2,-9]
# Output: 0
# Explanation: One optimal partition is: [2,4,-9] and [-1,0,-2].
# The absolute difference between the sums of the arrays is abs((2 + 4 + -9) - (-1 + 0 + -2)) = 0.

import sys
def minSumDiff(idx,s1,s2,c1,c2):
    # print("calling",idx,s1,s2,c1,c2)

    if idx >= n:
        return abs(s1-s2)
    
    if (idx,s1,s2) in memo:
        return memo[idx,s1,s2]
    min_diff = sys.maxsize
    if c1 < hn:
        min_diff = min(min_diff,minSumDiff(idx+1,s1+nums[idx],s2,c1+1,c2))
    if c2 < hn:
        min_diff = min(min_diff,minSumDiff(idx+1,s1,s2+nums[idx],c1,c2+1))

    memo[idx,s1,s2] = min_diff
    return min_diff



if __name__ == "__main__":
    nums = [3,9,7,3]
    n = len(nums)
    hn = n//2
    memo = {}
    print(minSumDiff(0,0,0,0,0))

    nums = [2,-1,0,4,-2,-9]
    n = len(nums)
    hn = n//2
    memo = {}
    print(minSumDiff(0,0,0,0,0))