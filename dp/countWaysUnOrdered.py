# Count ways unordered
# Here order of summaition does not matter


# O(n*n*n)
def countUnOrdered(min,n):
    if n == 0:
        return 1

    ans = 0
    if (min,n) in memo:
        return memo[min,n]
    # adding all the counts with min starting min to n
    for i in range(min,n+1):
        ans += countUnOrdered(i,n-i)

    memo[min,n] = ans
    return ans

# O(n*n)
def countUnOrdered2(min,n):
    if n == 0:
        return 1
    if min > n:
        return 0
    if min == n:
        return 1
    
    if (min,n) in memo:
        return memo[min,n]
    ans = countUnOrdered2(min,n-min) + countUnOrdered2(min+1,n)
    memo[min,n] = ans
    return ans


# O(n*n)
def countUnOrderedSetTab(n):
    dp = [0 for i in range(n+1)]
    dp[0] = 1

    for i in range(1,n+1):
        for j in range(i,n+1):
            dp[j] += dp[j-i]
        # print(dp)
    
    return dp[-1]

def countUnOrderedSetTab2(n):
    dp = [0 for i in range(n+1)]
    dp[0] = 1
    
    for i in range(n,0,-1):
        for j in range(i,n+1):
            dp[j] += dp[j-i]
    
    # print(dp)
    return dp[-1]

if __name__ == "__main__":

    for i in range(1,11):
        memo = {}
        print("Top Down For",i,"is",countUnOrdered(1,i))
        memo = {}
        print("Top Down2 For",i,"is",countUnOrdered2(1,i))
        print("Bottom Up For",i,"is",countUnOrderedSetTab(i))
        print("Bottom Up For",i,"is",countUnOrderedSetTab2(i))
    