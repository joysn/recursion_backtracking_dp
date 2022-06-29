# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d40bb
# Dr. Patel has N stacks of plates. Each stack contains K plates. Each plate has a positive beauty value, 
# describing how beautiful it looks.

# Dr. Patel would like to take exactly P plates to use for dinner tonight. If he would like to take a plate in 
# a stack, he must also take all of the plates above it in that stack as well.

# Help Dr. Patel pick the P plates that would maximize the total sum of beauty values.

# Input
# The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a 
# line containing the three integers N, K and P. Then, N lines follow. The i-th line contains K integers, describing 
# the beauty values of each stack of plates from top to bottom.

# Output
# For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y 
# is the maximum total sum of beauty values that Dr. Patel could pick.


# N,K,P 2 4 5

# 10 10 100 30
# 80 50 10 50
# Output - Case #1: 250

# N,K,P = 3 2 3
# 80 80
# 15 50
# 20 10
# Case #2: 180

def maxBeauty(n,k,p):
    if p == 0:
        return 0
    if k >= K or n >= N:
        return 0
    
    # Include
    next_k = (k+1)%K
    next_n = n + (k+1)//K
    # next_k = k+(n+1)//N
    # next_n = (n+1)%N
    beauty_max = max(beauty[n][k] + maxBeauty(next_n,next_k,p-1),maxBeauty(n+1,k,p))

    # print(n,k,p,beauty_max)
    return beauty_max

def maxBeautyTab():
    beautyPrefix = [[0 for i in range(K+1)] for j in range(N+1)]

    for i in range(1,N+1):
        for j in range(1,K+1):
            beautyPrefix[i][j] = beauty[i][j] + beautyPrefix[i][j-1]
    # for e in beautyPrefix:
    #     print(e)

    dp = [[0 for i in range(P+1)] for j in range(N+1)]

    for i in range(1,N+1):
        for j in range(1,P+1):
            # dp[i][j]
            # Pick j plates from first i rows
            for x in range(min(K,j)+1):
                dp[i][j] = max(dp[i][j],beautyPrefix[i][x]+dp[i-1][j-x])

    return dp[N][P]


if __name__ == "__main__":

    N,K,P = 2, 4, 5
    beauty = [
        [0, 0, 0, 0, 0]
        ,[0, 10, 10, 100, 30]
        ,[0, 80, 50, 10, 50]
    ]
    # Output - 250
    # print(maxBeauty(0,0,P))
    print(maxBeautyTab())
    


    N,K,P = 3,2,3
    beauty = [
        [0,0,0],
        [0,80,80],
        [0,15,50],
        [0,20,10]
    ]
    # Case #2: 180
    # print(maxBeauty(0,0,0))
    print(maxBeautyTab())