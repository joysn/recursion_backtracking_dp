# Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/
# 300. Longest Increasing Subsequence
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order
#  of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# Example 2:
# Input: nums = [0,1,0,3,2,3]
# Output: 4

# Example 3:
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1

def longestSub(idx):
    
    if idx == n-1:
        return 1

    if idx in memo:
        return memo[idx]
    maxcnt = 0
    if nums[idx+1] > nums[idx]:
        maxcnt = max(maxcnt, 1+longestSub(idx+1))
    else:
        maxcnt = max(maxcnt, longestSub(idx+1))

    memo[idx] = maxcnt
    return maxcnt


# Runtime: 3191 ms, faster than 63.57% of Python3 online submissions for Longest Increasing Subsequence.
# Memory Usage: 14.3 MB, less than 13.94% of Python3 online submissions for Longest Increasing Subsequence.

def longestSubTab():
    dp = [1 for i in range(n)]
    maxcnt = 1
    dp[n-1] = 1
    for i in range(n-2,-1,-1):
        for j in range(i+1,n):
            if nums[j] > nums[i]:
                # if dp[j]+1 > dp[i]:
                dp[i] = max(dp[i],dp[j]+1)
                maxcnt = max(maxcnt,dp[i])
        
    # print(dp)
    return maxcnt

if __name__ == "__main__":
    nums = [7, 49, 23, 8, 30, 22, 44, 28, 23, 9, 40, 15]
    n = len(nums)
    memo = {}
    print(longestSub(0))
    print(longestSubTab())

    nums = [1,2,3,4]
    n = len(nums)
    memo = {}
    print(longestSub(0))
    print(longestSubTab())

    nums = [1,2,3,3,5,6,5,7,6,8]
    n = len(nums)
    memo = {}
    print(longestSub(0))
    print(longestSubTab())