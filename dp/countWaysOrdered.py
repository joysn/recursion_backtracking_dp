# Ordered Sets - given n, find the number of ways in which the number can be formed using other numbers
# Since order matters, so
# F(1) = 1
# F(2) = 1+1, 2
# F(3) = 1+1+1,1+2,2+1,3

def countOrderedSet(n):
    if n == 0:
        return 1

    if memo[n] != -1:
        return memo[n]
    ans = 0
    for i in range(1,n+1):
        ans += countOrderedSet(n-i)

    memo[n] = ans
    return ans

def countOrderedSetTab(n):

    dp = [0 for i in range(n+1)]
    dp[0] = 1
    
    sum = 0
    for i in range(1,n+1):
        dp[i] = sum + 1
        sum += dp[i]
        
    # print(dp)
    return dp[-1]

if __name__ == "__main__":

    for i in range(1,7):
        memo = [-1 for j in range(i+1)]
        print("Top Down For",i,"is",countOrderedSet(i))
        print("Bottom Up",i,"is",countOrderedSetTab(i))
        print("No logic",2**(i-1))