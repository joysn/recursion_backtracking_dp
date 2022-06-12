# In IPL 2025, the amount that each player is paid varies from match to match. The match fee depends on the quality of opposition, 
# the venue etc.
# The match fees for each match in the new season have been announced in advance. Each team has to enforce a mandatory rotation policy 
# so that no player ever plays three matches in a row during the season.
# Nikhil is the captain and chooses the team for each match. He wants to allocate a playing schedule for himself to 
# maximize his earnings through match fees during the season.

# Input format
# Line 1: A single integer N, the number of games in the IPL season.
# Line 2: N non-negative integers, where the integer in position i represents the fee for match i.

# Output format
# The output consists of a single non-negative integer, the maximum amount of money that Nikhil can earn during this IPL season.

# Sample Input 1
# 5 
# 10 3 5 7 3 
# Sample Output 1
# 23
# (Explanation: 10+3+7+3)

# Sample Input 2
# 8
# 3 2 3 2 3 5 1 3
# Sample Output 2
# 17
# (Explanation: 3+3+3+5+3)

def maxIPLFees(idx):
    global fees, n, memo, count
    count += 1

    if idx >= n:
        return 0
    
    if memo[idx] != 0:
        return memo[idx]

    if idx == n-1:
        memo[idx] = fees[idx]
        return memo[idx]
    if idx == n-2:
        memo[idx] = fees[idx]+fees[idx+1]
        return memo[idx]
    
    memo[idx] = max((fees[idx]+maxIPLFees(idx+2)),(fees[idx+1]+maxIPLFees(idx+2)),(fees[idx]+fees[idx+1]+maxIPLFees(idx+3)))
    return memo[idx]

def maxIPLFeesTab():
    # This is complemenatory of minSUPWtab()
    global n, fees
    dp = [0 for i in range(n)]
    dp[0] = fees[0]
    dp[1] = fees[1]
    dp[2] = fees[2]

    for i in range(3,n):
        dp[i] = min(dp[i-1],dp[i-2],dp[i-3]) + fees[i]
    
    return sum(fees) - min(dp[n-1],dp[n-2],dp[n-3])

if __name__ == "__main__":
    n = 5
    count = 0
    memo = [0 for i in range(n)]
    fees = [10,3,5,7,3]

    if n <= 2:
        print("For Fees", fees, "The max IPL earning is",sum(fees))
    else:    
        print("For Fees", fees, "The max IPL earning is",maxIPLFees(0),"Count:",count)
        print("For Fees", fees, "The max IPL earning is",maxIPLFeesTab())

    n = 8
    count = 0
    memo = [0 for i in range(n)]
    fees = [3, 2, 3, 2, 3, 5, 1, 3]
    if n <= 2:
        print("For Fees", fees, "The max IPL earning is",sum(fees))
    else:    
        print("For Fees", fees, "The max IPL earning is",maxIPLFees(0),"Count:",count)
        print("For Fees", fees, "The max IPL earning is",maxIPLFeesTab())

