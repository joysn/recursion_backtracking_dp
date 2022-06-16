# Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with 
# sum equal to given sum. 
# The numbers can be taken as many times as required
# Same as Coin Change

def ifSubsetSumRepeating(idx, csum):
    global nums, n
    if csum < 0:
        return False
    if csum == 0:
        return True
    if idx >= n:
        return False

    if memo[idx][csum] != None:
        return memo[idx][csum]
    if nums[idx] <= csum:
        if ifSubsetSumRepeating(idx,csum-nums[idx]):
            memo[idx][csum] = True
            return True
    if ifSubsetSumRepeating(idx+1,csum):
        memo[idx][csum] = True
        return True

    memo[idx][csum] = False
    return False

def printSubsetSumRepeating(idx,csum):
    global nums, n
    if csum == 0:
        # print(",",end="")
        return
    if idx >= n:
        return
    # if nums[idx] <= csum:
    if ifSubsetSumRepeating(idx,csum-nums[idx]):
        print(nums[idx],end=" ")
        printSubsetSumRepeating(idx,csum-nums[idx])
    elif ifSubsetSumRepeating(idx+1,csum):
        printSubsetSumRepeating(idx+1,csum)
    
    return

def ifSubsetSumRepeatingTab(sum):
    global nums
    if sum == 0:
        return True

    dp = [False for i in range(sum+1)]
    dp[0] = True

    for i in range(sum+1):
        if dp[i]:
            for num in nums:
                if i + num <= sum:
                    dp[i+num] = True
                    if i+num == sum:
                        # print(dp)
                        return True
    
    # print(dp)
    return dp[sum]

if __name__ == "__main__":
    nums = [2,7,4,5,19]
    sum = 12
    n = len(nums)
    memo = [[None for i in range(sum+1)] for j in range(n)]
    print("Top Down:",ifSubsetSumRepeating(0,sum))
    print("Tabular:",ifSubsetSumRepeatingTab(sum))
    print("Top Down Print:",end="")
    printSubsetSumRepeating(0,sum)
    print("\n*************************************")



    nums = [12,17,4,5,19]
    sum = 7
    n = len(nums)
    memo = [[None for i in range(sum+1)] for j in range(n)]
    print(ifSubsetSumRepeating(0,sum))
    print("Tabular:",ifSubsetSumRepeatingTab(sum))
    print("Top Down Print:",end="")
    printSubsetSumRepeating(0,sum)
    print("\n*************************************")