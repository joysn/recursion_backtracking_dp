# Given a number n, count minimum steps to minimize it to 1 according to the following criteria: 

# If n is divisible by 2 then we may reduce n to n/2.
# If n is divisible by 3 then you may reduce n to n/3.
# Decrement n by 1.
# Examples: 

# Input : n = 10
# Output : 3

# Input : 6
# Output : 2

def minStepsToOne(n):
    global count, memo
    count += 1
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 1
    
    if memo[n] != -1:
        return memo[n]
    if n%2==0 and n%3 == 0:
        memo[n] = min((1+minStepsToOne(n-1)),(1+minStepsToOne(int(n/2))),(1+minStepsToOne(int(n/3))))
    elif n%2 == 0:
        memo[n] = min((1+minStepsToOne(n-1)),(1+minStepsToOne(int(n/2))))
    elif n%3 == 0:
        memo[n] = min((1+minStepsToOne(n-1)),(1+minStepsToOne(int(n/3))))
    else:
        memo[n] = 1+minStepsToOne(n-1)
    return memo[n]

def minStepsToOneTab(n):

    dp = [-1 for i in range(n+1)]
    dp[0] = 0
    dp[1] = 0
    
    for i in range(2,n+1):
        if i%2 == 0 and i%3 == 0:
            dp[i] = min(dp[i-1]+1, dp[int(i/2)]+1, dp[int(i/3)]+1)
            # print("1st ",i,dp[i])
        elif i%2 == 0:
            dp[i] = min(dp[i-1]+1, dp[int(i/2)]+1)
            # print("2nd ",i,dp[i])
        elif i%3 == 0:
            dp[i] = min(dp[i-1]+1, dp[int(i/3)]+1)
            # print("3rd ",i,dp[i])
        else:
            dp[i] = dp[i-1]+1
            # print("4th ",i,dp[i])
    
    # print(dp)
    return dp[n]


if __name__== "__main__":

    count = 0
    n = 10
    memo = [-1 for i in range(n+1)]
    print("For",n, "Min step to reach is",minStepsToOne(n),count)
    print("For",n, "Min step to reach is",minStepsToOneTab(n))

    count = 0
    n = 6
    memo = [-1 for i in range(n+1)]
    print("For",n, "Min step to reach is",minStepsToOne(n),count)
    print("For",n, "Min step to reach is",minStepsToOneTab(n))