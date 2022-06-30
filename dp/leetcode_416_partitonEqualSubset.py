# https://leetcode.com/problems/partition-equal-subset-sum/
# 416. Partition Equal Subset Sum
# Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

# Example 1:
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].

# Example 2:
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.


def ifEqualSubset(idx,csum):
    if csum == s//2:
        return True
    if idx == n or csum > s//2:
        return False

    if memo[idx][csum] != -1:
        return memo[idx][csum]
    ans = False
    csum += nums[idx]
    ans |= ifEqualSubset(idx+1,csum)
    csum -= nums[idx]
    ans |= ifEqualSubset(idx+1,csum)

    memo[idx][csum] = ans
    return ans
    
def ifEqualSubsetTab():

    if s%2 != 0:
        return False

    dp = [0 for i in range(hs+1)]
    dp[0] = 1
    for i in range(n):
        for j in range(hs,0,-1):
            if j-nums[i] >= 0:
                dp[j] |= dp[j-nums[i]]
    # print(dp)
    return dp[-1] == 1
    


if __name__=="__main__":
    nums = [1,5,11,5]
    n = len(nums)
    s = sum(nums)
    hs = s//2
    if s%2 != 0:
        print("False")
    else:
        memo = [[-1 for i in range(hs+1)] for j in range(n)]
        print("Top Down",ifEqualSubset(0,0))
    print("Bottom Up",ifEqualSubsetTab())

    nums = [1,2,3,5]
    n = len(nums)
    s = sum(nums)
    hs = s//2
    if s%2 != 0:
        print("Top Down False")
    else:
        memo = [[-1 for i in range(s//2+1)] for j in range(n)]
        print("Top Down",ifEqualSubset(0,0))
    print("Bottom Up",ifEqualSubsetTab())

    nums = [1,2,2,1,5,1]
    n = len(nums)
    s = sum(nums)
    hs = s//2
    if s%2 != 0:
        print("False")
    else:
        memo = [[-1 for i in range(s//2+1)] for j in range(n)]
        print("Top Down",ifEqualSubset(0,0))
    print("Bottom Up",ifEqualSubsetTab())

    nums = [4,2,8]
    n = len(nums)
    s = sum(nums)
    hs = s//2
    if s%2 != 0:
        print("False")
    else:
        memo = [[-1 for i in range(s//2+1)] for j in range(n)]
        print("Top Down",ifEqualSubset(0,0))
    print("Bottom Up",ifEqualSubsetTab())

    nums = [1,2,3,4,5,6,7]
    n = len(nums)
    s = sum(nums)
    hs = s//2
    if s%2 != 0:
        print("False")
    else:
        memo = [[-1 for i in range(s//2+1)] for j in range(n)]
        print("Top Down",ifEqualSubset(0,0))
    print("Bottom Up",ifEqualSubsetTab())
