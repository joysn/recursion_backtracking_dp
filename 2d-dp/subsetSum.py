# Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with 
# sum equal to given sum. 

# Example: 

# Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
# Output: True  
# There is a subset (4, 5) with sum 9.

# Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
# Output: False
# There is no subset that add up to 30.


def ifSubsetSum(idx, csum):
    global nums

    if csum < 0:
        return False
    if csum == 0:
        return True
    if idx >= n:
        return False
    
    # print("Sudipto",idx,csum)
    if memo[idx][csum] != None:
        return memo[idx][csum]
    if nums[idx] <= csum:
        if ifSubsetSum(idx+1,csum-nums[idx]):
            memo[idx][csum] = True
            return True
    if ifSubsetSum(idx+1,csum):
        memo[idx][csum] = True
        return True

    memo[idx][csum] = False
    return False

def printSubsetSum(idx, csum):
    global nums
    if csum == 0:
        print(",",end="")
        return
    if idx >= n:
        return
    
    if ifSubsetSum(idx+1,csum-nums[idx]):
        print(nums[idx],end=" ")
        printSubsetSum(idx+1,csum-nums[idx])
    if ifSubsetSum(idx+1,csum):
        printSubsetSum(idx+1,csum)

def ifSubsetSumTab():
    global nums, sum, n
    dp = [[False for i in range(sum+1)] for j in range(n+1)]

    dp[0][0] = 1 # 0 sum possible with 0th nums
    for row in range(n+1):
        dp[row][0] = True

    for col in range(1,sum+1):
        dp[0][col] = False

    for r in range(1,n+1):
        for c in range(1,sum+1):
            dp[r][c] = dp[r-1][c] 
            if c-nums[r-1] >= 0:
                dp[r][c] = dp[r][c] or dp[r-1][c-nums[r-1]]

            # if c == sum and dp[r][c] == True:
            #     return True
    
    # for i in range(n+1):
    #     print(dp[i])
    return dp[n][sum]


def ifSubsetSumTab1():
    global nums, sum, n
    dp = [[False for i in range(sum+1)] for j in range(2)]

    dp[0][0] = 1 # 0 sum possible with 0th nums
    for row in range(2):
        dp[row][0] = True

    for col in range(1,sum+1):
        dp[0][col] = False

    for r in range(1,n+1):
        for c in range(1,sum+1):
            dp[1][c] = dp[0][c] 
            if c-nums[r-1] >= 0:
                dp[1][c] |=  dp[0][c-nums[r-1]]

        # Copy to 0th rows
        for k in range(sum+1):
            dp[0][k] = dp[1][k]
    # for i in range(2):
    #     print(dp[i])

    return dp[1][sum]


def ifSubsetSumTab2():
    global nums, sum, n
    dp = [False for j in range(sum+1)]

    dp[0] = True # 0 sum possible with 0th nums
    
    for i in range(n):
        for s in range(sum,0,-1):
            if s-nums[i] >= 0:
                dp[s] |= dp[s-nums[i]]
    
    return dp[sum]

if __name__ == "__main__":
    nums = [2,7,4,5,19]
    sum = 12
    n = len(nums)
    memo = [[None for i in range(sum+1)] for j in range(n)]
    print("Top Down",ifSubsetSum(0,sum))
    print("Tabular:",ifSubsetSumTab())
    print("Tabular Mem Optimize:",ifSubsetSumTab1())
    print("Tabular Mem Optimize2:",ifSubsetSumTab2())
    print("Top Down print:",end="")
    printSubsetSum(0,sum)
    print("\n***********************************************************")

    nums = [2,7,4,5,19]
    sum = 22
    n = len(nums)
    memo = [[None for i in range(sum+1)] for j in range(n)]
    print("Top Down",ifSubsetSum(0,sum))
    print("Tabular:",ifSubsetSumTab())
    print("Tabular Mem Optimize:",ifSubsetSumTab1())
    print("Tabular Mem Optimize2:",ifSubsetSumTab2())
    print("Top Down print:",end="")
    printSubsetSum(0,sum)
    print("\n***********************************************************")

    nums = [3, 34, 4, 12, 5, 2]
    sum = 9
    n = len(nums)
    memo = [[None for i in range(sum+1)] for j in range(n)]
    print("Top Down",ifSubsetSum(0,sum))
    print("Tabular:",ifSubsetSumTab())
    print("Tabular Mem Optimize:",ifSubsetSumTab1())
    print("Tabular Mem Optimize2:",ifSubsetSumTab2())
    print("Top Down print:",end="")
    printSubsetSum(0,sum)
    print("\n***********************************************************")

    nums = [3, 34, 4, 12, 5, 2]
    sum = 30
    n = len(nums)
    memo = [[None for i in range(sum+1)] for j in range(n)]
    print("Top Down",ifSubsetSum(0,sum))
    print("Tabular:",ifSubsetSumTab())
    print("Tabular Mem Optimize:",ifSubsetSumTab1())
    print("Tabular Mem Optimize2:",ifSubsetSumTab2())
    print("Top Down print:",end="")
    printSubsetSum(0,sum)
    print("\n***********************************************************")