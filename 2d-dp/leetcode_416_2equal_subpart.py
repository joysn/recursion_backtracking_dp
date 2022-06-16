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


def splitEqualSubbarray(idx, csum):
    global n, nums
    if csum == 0:
        return True
    if idx >= n:
        return False

    if memo[idx][csum] != None:
        return memo[idx][csum]
    if splitEqualSubbarray(idx+1,csum-nums[idx]):
        memo[idx][csum] = True
        return True
    if splitEqualSubbarray(idx+1, csum):
        memo[idx][csum] = True
        return True

    memo[idx][csum] = False
    return False

def splitEqualSubbarrayTab():
    global nums, n, hsum

    dp = [[0 for i in range(hsum+1)] for j in range(n+1)]
    dp[0][0] = 1
    for i in range(n+1):
        dp[i][0] = 1

    for i in range(1,n+1):
        for j in range(hsum+1):
            dp[i][j] = dp[i-1][j]
            if j-nums[i-1] >= 0:
                dp[i][j] |= dp[i-1][j-nums[i-1]]
    
    # print(dp)
    return dp[n][hsum] == 1

def splitEqualSubbarrayTab1():
    global nums, n, hsum

    dp = [[0 for i in range(hsum+1)] for j in range(2)]
    dp[0][0] = 1
    dp[1][0] = 1

    for i in range(1,n+1):
        for j in range(hsum+1):
            dp[1][j] = dp[0][j]
            if j-nums[i-1] >= 0:
                dp[1][j] |= dp[0][j-nums[i-1]]
        for k in range(hsum+1):
            dp[0][k] = dp[1][k]

    return dp[1][hsum] == 1

def splitEqualSubbarrayTab2():
    global nums, n, hsum

    dp = [0 for i in range(hsum+1)]
    dp[0] = 1

    for i in range(n):
        for j in range(hsum,0,-1):
            if j-nums[i] >= 0:
                dp[j] |= dp[j-nums[i]]

    # print(dp)
    return dp[hsum] == 1

if __name__ == "__main__":
    nums = [1,5,11,5]
    n = len(nums)
    s = sum(nums)
    if s%2 != 0:
        print("Not possible to split into 2 equal sum subarray",nums)
    else:
        hsum = sum(nums)//2
        memo = [[None for i in range(hsum+1)] for j in range(n)]
        print("Split Equal Subarray:",splitEqualSubbarray(0,hsum))
        print("Bottom Up",splitEqualSubbarrayTab())
        print("Bottom Up1",splitEqualSubbarrayTab1())
        print("Bottom Up2",splitEqualSubbarrayTab2())


    nums = [1,2,3,5]
    n = len(nums)
    s = sum(nums)
    if s%2 != 0:
        print("Not possible to split into 2 equal sum subarray",nums)
    else:
        hsum = sum(nums)//2
        memo = [[None for i in range(hsum+1)] for j in range(n)]
        print("Split Equal Subarray:",splitEqualSubbarray(0,hsum))
        print("Bottom Up",splitEqualSubbarrayTab())
        print("Bottom Up1",splitEqualSubbarrayTab1())
        print("Bottom Up2",splitEqualSubbarrayTab2())

    nums = [4,4,4,4,4,4,4,4,8,8,8,8,8,8,8,8,12,12,12,12,12,12,12,12,16,16,16,16,16,16,16,16,20,20,20,20,20,20,20,20,24,24,24,24,24,24,24,24,28,28,28,28,28,28,28,28,32,32,32,32,32,32,32,32,36,36,36,36,36,36,36,36,40,40,40,40,40,40,40,40,44,44,44,44,44,44,44,44,48,48,48,48,48,48,48,48,52,52,52,52,52,52,52,52,56,56,56,56,56,56,56,56,60,60,60,60,60,60,60,60,64,64,64,64,64,64,64,64,68,68,68,68,68,68,68,68,72,72,72,72,72,72,72,72,76,76,76,76,76,76,76,76,80,80,80,80,80,80,80,80,84,84,84,84,84,84,84,84,88,88,88,88,88,88,88,88,92,92,92,92,92,92,92,92,96,96,96,96,96,96,96,96,97,99]
    n = len(nums)
    s = sum(nums)
    if s%2 != 0:
        print("Not possible to split into 2 equal sum subarray",nums)
    else:
        hsum = sum(nums)//2
        memo = [[None for i in range(hsum+1)] for j in range(n)]
        print("Split Equal Subarray:",splitEqualSubbarray(0,hsum))
        print("Bottom Up",splitEqualSubbarrayTab())
        print("Bottom Up1",splitEqualSubbarrayTab1())
        print("Bottom Up2",splitEqualSubbarrayTab2())
