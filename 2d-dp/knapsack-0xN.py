# 0/N Knapsack Problem

def knapsack(idx,csize):
    # print("Calling",idx,csize)
    
    if idx >= n:
        return 0
    if csize == 0:
        return 0

    if memo[idx-1][csize-1] != -1:
        return memo[idx-1][csize-1]
    max_val = 0
    if sizes[idx] <= csize:
        max_val = values[idx] + knapsack(idx,csize-sizes[idx])
    max_val = max(max_val,knapsack(idx+1,csize))
    
    memo[idx-1][csize-1] = max_val
    return max_val

def knapsack1(idx,csize):

    if idx < 0:
        return 0
    if csize == 0:
        return values[idx]

    if memo[idx][csize-1] != -1:
        return memo[idx][csize-1]
    max_val = 0
    if sizes[idx] <= csize:
        max_val = values[idx] + knapsack(idx,csize-sizes[idx])
    max_val = max(max_val, knapsack(idx-1,csize))

    memo[idx][csize-1] = max_val
    return max_val

def knapsackTab():
    
    dp = [[0 for i in range(size+1)] for j in range(n)]

    for i in range(n):
        for s in range(size+1):
            if i-1>= 0:
                dp[i][s] = dp[i-1][s]
            if s-sizes[i] >= 0:
                dp[i][s] = max(dp[i][s-sizes[i]]+values[i], dp[i][s])

    return dp[-1][-1]

def knapsackTab2():
    dp = [0 for i in range(size+1)]

    for i in range(n):
        for s in range(size+1):
            if s-sizes[i] >= 0:
                dp[s] = max(dp[s-sizes[i]]+values[i], dp[s])
    
    return dp[-1]

if __name__ == "__main__":
    size = 4
    sizes = [3,2,2,1,2]
    values = [0,5,3,8,4]
    n = len(sizes)
    memo = [[-1 for s in range(size)] for i in range(n)]
    print("Going forward",knapsack(0,size))
    memo = [[-1 for s in range(size)] for i in range(n)]
    print("Going backward",knapsack1(n-1,size))
    print("Tabular",knapsackTab())
    print("Tabular2",knapsackTab2())

    size = 4
    sizes = [3,2,2]
    values = [30,15,18]
    n = len(sizes)

    memo = [[-1 for s in range(size)] for i in range(n)]
    print("Going forward",knapsack(0,size))
    memo = [[-1 for s in range(size)] for i in range(n)]
    print("Going backward",knapsack1(n-1,size))
    print("Tabular",knapsackTab())
    print("Tabular2",knapsackTab2())