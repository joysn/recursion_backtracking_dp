# http://poj.org/problem?id=2663
# In how many ways can you tile a 3xn rectangle with 2x1 dominoes?
# Here is a sample tiling of a 3x12 rectangle.

# Input

# Input consists of several test cases followed by a line containing -1. Each test case is a line containing an integer 0 <= n <= 30.
# Output

# For each test case, output one integer number giving the number of possible tilings.
# Sample Input

# 2
# 8
# 12
# -1
# Sample Output

# 3
# 153
# 2131

# Solution - https://www.youtube.com/watch?v=yn2jnmlepY8
def countWays3x(n):

    dp = [[0 for i in range(8)] for i in range(n+1)]
    dp[0][7] = 1

    for i in range(1,n+1):
        dp[i][0] += dp[i-1][7]

        dp[i][1] += dp[i-1][6]

        dp[i][2] += dp[i-1][5]

        dp[i][3] += dp[i-1][7]
        dp[i][3] += dp[i-1][4]

        dp[i][4] += dp[i-1][3]

        dp[i][5] += dp[i-1][2]

        dp[i][6] += dp[i-1][1]
        dp[i][6] += dp[i-1][7]

        dp[i][7] += dp[i-1][3]
        dp[i][7] += dp[i-1][6]
        dp[i][7] += dp[i-1][0]

    return dp[n][7]

if __name__=="__main__":

    print(countWays3x(2))
    print(countWays3x(8))
    print(countWays3x(12))