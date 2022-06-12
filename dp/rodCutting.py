# Given a rod of length n inches and an array of prices that includes prices of all pieces of size smaller than n. 
# Determine the maximum value obtainable by cutting up the rod and selling the pieces. 
# For example, if the length of the rod is 8 and the values of different pieces are given as the following, 
# then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6) 

# length   | 1   2   3   4   5   6   7   8  
# --------------------------------------------
# price    | 1   5   8   9  10  17  17  20
# And if the prices are as following, then the maximum obtainable value is 24 (by cutting in eight pieces of length 1) 

# length   | 1   2   3   4   5   6   7   8  
# --------------------------------------------
# price    | 3   5   8   9  10  17  17  20


def rodCuttingMaxPrice(n):
    global price, memo, count
    count += 1

    if n == 0:
        return 0

    if memo[n] != -1:
        return memo[n]
    if n == 1:
        memo[n] = price[1]
        return memo[n]

    ans = -1
    for i in range(1,n+1):
        ans = max(ans,price[i]+rodCuttingMaxPrice(n-i))
        
    memo[n] = ans
    return memo[n]

def rodCuttingMaxPriceTab():

    if n == 0:
        return 0
    if n == 1:
        return price[1]
    dp = [-1 for i in range(n+1)]
    dp[0] = 0
    dp[1] = price[1]

    for i in range(2,n+1):
        max = dp[0] + price[i]
        for j in range(1,i//2 + 1):
            p = dp[j] + dp[i-j]
            if p > max:
                max = p
        dp[i] = max
    
    # print(dp)
    return dp[n]

if __name__ == "__main__":

    price = [0,1,5,8,9,10,17,17,20]
    for i in range(0,9):
        n = i
        memo = [-1 for j in range(n+1)]
        count = 0
        print("Price:", price[:i],"n:",n, "Max Price:", rodCuttingMaxPrice(n))
        print("Price:", price[:i],"n:",n, "Max Price Tabular:", rodCuttingMaxPriceTab())
    
    price = [0,3,5,8,9,10,17,17,20]
    n = len(price)-1
    memo = [-1 for i in range(n+1)]
    count = 0
    print(rodCuttingMaxPrice(n))
    print(rodCuttingMaxPriceTab())


    price = [0,1,1,1,6]
    n = len(price)-1
    memo = [-1 for i in range(n+1)]
    count = 0
    print(rodCuttingMaxPrice(n))
    print(rodCuttingMaxPriceTab())


    price = [0,1,3,4,5,7,9,10,11]
    n = len(price)-1
    memo = [-1 for i in range(n+1)]
    count = 0
    print(rodCuttingMaxPrice(n))
    print(rodCuttingMaxPriceTab())
