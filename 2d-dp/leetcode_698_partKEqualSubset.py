# 698. Partition to K Equal Sum Subsets
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
# Given an integer array nums and an integer k, return true if it is possible to divide this array into k 
# non-empty subsets whose sums are all equal.

# Example 1:
# Input: nums = [4,3,2,3,5,2,1], k = 4
# Output: true
# Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

# Example 2:
# Input: nums = [1,2,3,4], k = 3
# Output: false

# Runtime: 226 ms, faster than 66.80% of Python3 online submissions for Partition to K Equal Sum Subsets.
# Memory Usage: 13.9 MB, less than 77.87% of Python3 online submissions for Partition to K Equal Sum Subsets.

import copy
def backtrack(idx):

    if idx >= len(nums):
        return len(set(bucket)) == 1

    for j in range(k):
        bucket[j] += nums[idx]
        if nums[idx] <= partSum and backtrack(idx+1):
            return True
        bucket[j] -= nums[idx]
        if bucket[j] == 0:
            break
    return False
    

def partKEqualSubset():
    global bucket
    global partSum
    s = sum(nums)
    nums.sort(reverse=True)
    partSum = s//k
    if s%k != 0 or partSum < nums[0]:
        return False
    bucket = [0]*k
    
    return backtrack(0)
        



if __name__=="__main__":
    nums = [4,3,2,3,5,2,1]
    k = 4
    print(partKEqualSubset())

    nums = [1,2,3,4]
    k = 3
    print(partKEqualSubset())

    nums = [2,2,2,2,3,4,5]
    k = 4
    print(partKEqualSubset())

    nums = [2,2,2,1,1,3,4,5]
    k = 4
    print(partKEqualSubset())

    nums = [1,1,1,1,2,2,2,2]
    k = 4
    print(partKEqualSubset())