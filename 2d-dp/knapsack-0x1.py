# 0/1 Knapsack


def knapsack(idx,csize):
    global sizes, values, n, memo

    if idx >= n:
        return 0

    if memo[idx][csize-1] != -1:
        return memo[idx][csize-1]
    max_value = 0
    # Inlcude
    if sizes[idx] <= csize:
        max_value = values[idx] + knapsack(idx+1,csize-sizes[idx])

    # Exclude
    value = knapsack(idx+1,csize)
    if value > max_value:
            max_value = value

    memo[idx][csize-1] = max_value
    return memo[idx][csize-1]

def knapsack1(idx,csize):
    global sizes, values, n, memo

    if idx == 0:
        return 0

    if memo[idx][csize] != -1:
        return memo[idx][csize]
    max_value = 0
    # Inlcude
    if sizes[idx] <= csize:
        max_value = values[idx] + knapsack1(idx-1,csize-sizes[idx])

    # Exclude
    value = knapsack1(idx-1,csize)
    if value > max_value:
            max_value = value

    memo[idx][csize] = max_value
    return memo[idx][csize]

def knapsackTab():
    global size, sizes, values
    n = len(values)

    dp = [[0 for i in range(size+1)] for j in range(n+1)]

    for i in range(1,n+1):
        for s in range(size,-1,-1):
            if s >= sizes[i-1]:
                dp[i][s] = max(dp[i-1][s],values[i-1]+dp[i-1][s-sizes[i-1]])
        # print(dp[i])
    return dp[-1][-1]

def knapsackTab2():
    global size, sizes, values
    n = len(values)

    dp = [0 for i in range(size+1)]

    for i in range(1,n+1):
        for s in range(size,-1,-1):
            if s >= sizes[i-1]:
                dp[s] = max(dp[s],values[i-1]+dp[s-sizes[i-1]])
        # print(dp)
    return dp[-1]

if __name__ == "__main__":
    size = 4
    sizes = [3,2,2,1,2]
    values = [0,5,3,8,4]
    n = len(sizes)
    memo = [[-1 for s in range(size)] for i in range(n)]
    print("Going forward",knapsack(0,size))
    memo = [[-1 for s in range(size+1)] for i in range(n)]
    print("Going backward",knapsack1(n-1,size))
    print("Tabular",knapsackTab())
    print("Tabular2",knapsackTab2())

    size = 4
    sizes = [3,2,2]
    values = [30,15,18]
    n = len(sizes)

    memo = [[-1 for s in range(size)] for i in range(n)]
    print("Going forward",knapsack(0,size))
    memo = [[-1 for s in range(size+1)] for i in range(n)]
    print("Going backward",knapsack1(n-1,size))
    print("Tabular",knapsackTab())
    print("Tabular2",knapsackTab2())