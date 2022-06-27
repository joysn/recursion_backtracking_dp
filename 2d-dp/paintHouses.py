# Paint Houses
# Question: There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. 
# The cost of painting each house with a certain color is different. You have to paint all the houses such that no 
# two adjacent houses have the same color. The cost of painting each house with a certain color is represented 
# by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] 
# is the cost of painting house 1 with color green, and so on.
# Find the minimum cost to paint all houses.

import sys

def paintHouse(hidx,cidx):
    if hidx >= n:
        return 0
    
    if dp[cidx][hidx] != -1:
        return dp[cidx][hidx]
    min_cost = min(\
        cost[cidx][hidx]+paintHouse(hidx+1,(cidx+1)%K)\
        , cost[cidx][hidx]+paintHouse(hidx+1,(cidx+2)%K)\
        )
    dp[cidx][hidx] = min_cost
    return min_cost

# Execution Time - n*K*K
# Space - n*K
def paintHouseTab():
    dp = [[-1 for c in range(K)] for h in range(n)]
    for c in range(K):
        dp[0][c] = cost[c][0]
    
    
    for hidx in range(1,n):
        for cidx in range(K):
            min_cost = min(cost[cidx][hidx]+dp[hidx-1][c] for c in range(K) if c !=cidx)
            dp[hidx][cidx] = min_cost
    
    # for e in dp:
    #     print(e)
    return min(dp[-1])

# Reduce complexity by storing previous rows 2 min values
# Execution Time - n*K
# Space - n*K
def paintHouseTab2():
    dp = [[-1 for c in range(K)] for h in range(n)]
    min1 = sys.maxsize
    min2 = sys.maxsize
    for c in range(K):
        dp[0][c] = cost[c][0]
        if dp[0][c] <= min2:
            min2 = dp[0][c]
        if min2 < min1:
            min1, min2 = min2, min1
    
    for hidx in range(1,n):
        new_min1 = sys.maxsize
        new_min2 = sys.maxsize
        for cidx in range(K):
            if dp[hidx-1][cidx] == min1:
                min_cost = cost[cidx][hidx] + min2
            else:
                min_cost = cost[cidx][hidx] + min1
            dp[hidx][cidx] = min_cost
            if dp[hidx][cidx] <= new_min2:
                new_min2 = dp[hidx][cidx]
            if new_min2 < new_min1:
                new_min1, new_min2 = new_min2, new_min1
        min1 = new_min1
        min2 = new_min2
    
    # for e in dp:
    #     print(e)
    return min(dp[-1])
    

# Reduce space complexity by taking 1-d array only
# Execution Time - n*K
# Space - n
def paintHouseTab3():
    dp = [-1 for c in range(K)]
    min1 = sys.maxsize
    min2 = sys.maxsize
    for c in range(K):
        dp[c] = cost[c][0]
        if dp[c] <= min2:
            min2 = dp[c]
        if min2 < min1:
            min1, min2 = min2, min1
    
    for hidx in range(1,n):
        new_min1 = sys.maxsize
        new_min2 = sys.maxsize
        for cidx in range(K):
            if dp[cidx] == min1:
                min_cost = cost[cidx][hidx] + min2
            else:
                min_cost = cost[cidx][hidx] + min1
            dp[cidx] = min_cost
            if dp[cidx] <= new_min2:
                new_min2 = dp[cidx]
            if new_min2 < new_min1:
                new_min1, new_min2 = new_min2, new_min1
        min1 = new_min1
        min2 = new_min2
    
    # for e in dp:
    #     print(e)
    return min(dp)


if __name__ == "__main__":
    cost = [
        [14]
        ,[2]
        ,[11]
    ]
    K = len(cost)
    n = len(cost[0])
    min_cost = sys.maxsize
    dp = [[-1 for i in range(n)] for j in range(K)]
    for color in range(K):
        min_cost = min(min_cost,paintHouse(0,color))
    print("Top Down",min_cost)
    print("Bottom Up",paintHouseTab())
    print("Bottom Up-2",paintHouseTab2())
    print("Bottom Up-3",paintHouseTab3())

    cost = [
        [14,11,14]
        ,[2,14,3]
        ,[11,5,10]
    ]
    K = len(cost)
    n = len(cost[0])
    min_cost = sys.maxsize
    dp = [[-1 for i in range(n)] for j in range(K)]
    for color in range(K):
        min_cost = min(min_cost,paintHouse(0,color))
    print("Top Down",min_cost)
    print("Bottom Up",paintHouseTab())
    print("Bottom Up-2",paintHouseTab2())
    print("Bottom Up-3",paintHouseTab3())

    cost = [
        [14,11,14]
        ,[2,5,3]
        ,[11,14,10]
    ]
    K = len(cost)
    n = len(cost[0])
    min_cost = sys.maxsize
    dp = [[-1 for i in range(n)] for j in range(K)]
    for color in range(K):
        min_cost = min(min_cost,paintHouse(0,color))
    print("Top Down",min_cost)
    print("Bottom Up",paintHouseTab())
    print("Bottom Up-2",paintHouseTab2())
    print("Bottom Up-3",paintHouseTab3())

    cost = [
        [1,5,3,1]
        ,[5,8,2,2]
        ,[7,4,9,4]
    ]
    K = len(cost)
    n = len(cost[0])
    min_cost = sys.maxsize
    dp = [[-1 for i in range(n)] for j in range(K)]
    for color in range(K):
        min_cost = min(min_cost,paintHouse(0,color))
    print("Top Down",min_cost)
    print("Bottom Up",paintHouseTab())
    print("Bottom Up-2",paintHouseTab2())
    print("Bottom Up-3",paintHouseTab3())
