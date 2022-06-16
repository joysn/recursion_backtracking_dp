# https://codeforces.com/problemset/problem/577/B
# You are given a sequence of numbers a1, a2, ..., an, and a number m.

# Check if it is possible to choose a non-empty subsequence aij such that the sum of numbers in this subsequence is divisible by m.

# Input
# The first line contains two numbers, n and m (1 ≤ n ≤ 106, 2 ≤ m ≤ 103) — the size of the original sequence and 
# the number such that sum should be divisible by it.

# The second line contains n integers a1, a2, ..., an (0 ≤ ai ≤ 109).

# Output
# In the single line print either "YES" (without the quotes) if there exists the sought subsequence, 
# or "NO" (without the quotes), if such subsequence doesn't exist.

# Examples
# input - 5, [1 2 3]
# output - YES
# input - 6, [5]
# output - NO
# input - 6, [3 1 1 3]
# output - YES
# input - 6, [5 5 5 5 5 5]
# output  - YES

def subsetSumModulo(idx, csum):
    global nums, m, n

    if idx >= n:
        return False
    if csum%m == 0:
        return True
    
    if csum >= 0 and memo[idx][csum] != None:
        return memo[idx][csum]
    if subsetSumModulo(idx+1,csum+nums[idx]):
        memo[idx][csum] = True  if csum >= 0 else None
        return True
    if subsetSumModulo(idx+1,csum):
        memo[idx][csum] = True  if csum >= 0 else None
        return True

    memo[idx][csum] = False if csum >= 0 else None
    return False


def subsetSumModuleTab():
    global nums, n, m

    dp = [0 for i in range(m)]
    for a in nums:
        STemp = [0 for i in range(m)]
        for (i, v) in enumerate(dp):
            ii = (a + i) % m
            # dp[ii] - since we are just adding up the count and ultimately replace dp[ii] with new value
            # v = if we can reach i (i.e. if v>0), then (a+i)%5 also can be reached.
            STemp[ii] = dp[ii] + v
        STemp[a % m] = STemp[a % m] + 1 # Considering the number itself
        dp = STemp

    # print(dp)
    return dp[0] > 0,dp[0]
            


if __name__=="__main__":
    m = 5
    nums = [1,2,3]
    n = len(nums)
    memo = [[None for j in range(sum(nums)+1)] for i in range(n)]
    print("Top Down",subsetSumModulo(0,-1))
    print("Bottom Up:",subsetSumModuleTab())


    m = 6
    nums = [5]
    n = len(nums)
    memo = [[None for j in range(sum(nums)+1)] for i in range(n)]
    print("Top Down",subsetSumModulo(0,-1))
    print("Bottom Up:",subsetSumModuleTab())

    m = 6
    nums = [3,1,1,3]
    n = len(nums)
    memo = [[None for j in range(sum(nums)+1)] for i in range(n)]
    print("Top Down",subsetSumModulo(0,-1))
    print("Bottom Up:",subsetSumModuleTab())

    m = 6
    nums = [5,5,5,5,5,5]
    n = len(nums)
    memo = [[None for j in range(sum(nums)+1)] for i in range(n)]
    print("Top Down",subsetSumModulo(0,-1))
    print("Bottom Up:",subsetSumModuleTab())


    nums = [2, 6, 4, 3]
    m = 5
    n = len(nums)
    memo = [[None for j in range(sum(nums)+1)] for i in range(n)]
    print("Top Down",subsetSumModulo(0,-1))
    print("Bottom Up:",subsetSumModuleTab())