# Colorful knapsack

# You are given N stones, labeled from 1 to N. The i-th stone has the weight W[i]. There are M colors, 
# labeled by integers from 1 to M. The i-th stone has the color C[i] (of course, an integer between 1 to M, inclusive). 
# You want to fill a Knapsack with these stones. The Knapsack can hold a total weight of X. You want to select exactly M stones; 
# one of each color. The sum of the weights of the stones must not exceed X. Since you paid a premium for a Knapsack with capacity 
# X (as opposed to a Knapsack with a lower capacity), you want to fill the Knapsack as much as possible.
# Write a program that takes all the above values as input and calculates the best way to fill the Knapsack – that is, 
# the way that minimizes the unused capacity. Output this unused capacity.

# Input
# The first line of input contains the integer T, the number of test cases. Then follows the description of T test cases. 
# The first line of each test case contains three integers, N, M and X, separated by singlespace. The next line contains N integers, 
# W[1], W[2], W[3] … W[N], separated by single space. The next line contains N integers C[1], C[2], C[3] … C[N], separated by single space.

# Output
# An optimal way of filling the Knapsack minimizes unused capacity. There may be several optimal ways of filling the Knapsack. 
# Output the unused capacity of the Knapsack (a single integer on a line by itself) for an optimal way. 
# If there is no way to fill the Knapsack, output -1. Output T lines, one for each test case.

# Constraints
# 1 ≤ T ≤ 10
# 1 ≤ M ≤ 100
# M ≤ N ≤ 100
# 1 ≤ W[i] ≤ 100
# 1 ≤ C[i] ≤ M
# 1 ≤ X ≤ 10000

# Sample Input
# Case 1
# N M X
# 9 3 10
# 2 3 4 2 3 4 2 3 4
# 1 1 1 2 2 2 3 3 3

# Output - 0

# Case 2
# N M X
# 9 3 10
# 1 3 5 1 3 5 1 3 5
# 1 1 1 2 2 2 3 3 3
# Output: 1

# Case 3
# N M X
# 3 3 10
# 3 4 4
# 1 2 3
# Output - -1

# Case 4
# N M X
# 3 3 10
# 3 3 3
# 1 2 1

# Output - -1

def cknapsackTab():
    global pebbles
    dp = [[0 for i in range(X+1)] for j in range(M+1)]

    dp[0][0] = 1
    max_col = 0
    for midx in range(1,M+1):
        for x in range(X+1):
            for w in pebbles[midx]:
                if x-w>=0 and dp[midx-1][x-w] == 1:
                    dp[midx][x] = 1
                    if midx == M and x > max_col:
                        max_col = x
    # for e in dp:
    #     print(e)
    if max_col == 0:
        return -1
    return X-max_col

def cknapsackTab1():
    global pebbles
    dp = [[0 for i in range(X+1)] for j in range(2)]

    dp[0][0] = 1
    max_col = 0
    for midx in range(1,M+1):
        for x in range(X+1):
            for w in pebbles[midx]:
                if x-w>=0 and dp[0][x-w] == 1:
                    dp[1][x] = 1
                    if midx == M and x > max_col:
                        max_col = x
        for i in range(X+1):
            dp[0][i] = dp[1][i]
            dp[1][i] = 0

    if max_col == 0:
        return -1
    return X-max_col


if __name__ == "__main__":

    N = 9
    M = 3
    X = 10
    weights = [2, 3, 4, 2, 3, 4, 2, 3, 4]
    colors = [1, 1, 1, 2, 2, 2, 3, 3, 3]
    pebbles = dict()
    for i in range(M+1):
        pebbles[i] = []
    for id,c in enumerate(colors):
        pebbles[c].insert(-1,weights[id])
    # print(cknapsack(0,X))
    print(cknapsackTab())
    print(cknapsackTab1())

    N = 9
    M = 3
    X = 10
    weights = [1, 3, 5, 1, 3, 5, 1, 3, 5]
    colors = [1, 1, 1, 2, 2, 2, 3, 3, 3]
    pebbles = dict()
    for i in range(M+1):
        pebbles[i] = []
    for id,c in enumerate(colors):
        pebbles[c].insert(-1,weights[id])
    print(cknapsackTab())
    print(cknapsackTab1())

    N = 3
    M = 3
    X = 10
    weights = [3, 4, 4]
    colors = [1, 2, 3]
    pebbles = dict()
    for i in range(M+1):
        pebbles[i] = []
    for id,c in enumerate(colors):
        pebbles[c].insert(-1,weights[id])
    print(cknapsackTab())
    print(cknapsackTab1())


    N = 3
    M = 3
    X = 10
    weights = [3, 3, 3]
    colors = [1, 2, 1]
    pebbles = dict()
    for i in range(M+1):
        pebbles[i] = []
    for id,c in enumerate(colors):
        pebbles[c].insert(-1,weights[id])
    print(cknapsackTab())
    print(cknapsackTab1())