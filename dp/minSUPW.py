# In ICO School, all students have to participate regularly in SUPW. There is a different SUPW activity each day, and each activity has its own duration. The SUPW schedule for the next term has been announced, including information about the number of minutes taken by each activity.
# Nikhil has been designated SUPW coordinator. His task is to assign SUPW duties to students, including himself. The school's rules say that no student can go three days in a row without any SUPW duty.

# Nikhil wants to find an assignment of SUPW duty for himself that minimizes the number of minutes he spends overall on SUPW.

# Input format
# Line 1: A single integer N, the number of days in the future for which SUPW data is available.

# Line 2: N non-negative integers, where the integer in position i represents the number of minutes required for SUPW work on day i.

# Output format
# The output consists of a single non-negative integer, the minimum number of minutes that Nikhil needs to spend on SUPW duties this term

# Sample Input 1
# 10
# 3 2 1 1 2 3 1 3 2 1
# Sample Output 1
# 4
# (Explanation: 1+1+1+1)
# Sample Input 2
# 8
# 3 2 3 2 3 5 1 3
# Sample Output 2
# 5

def minSUPW(idx):
    global count
    global memo
    global time
    global n

    count += 1
    if idx >= n:
        return 0

    if memo[idx] != -1:
        return memo[idx]
    if idx >= n-2:
        memo[idx] = 0
        return memo[idx]

    # print(idx)
    memo[idx] = min((time[idx]+minSUPW(idx+1)), (time[idx+1]+minSUPW(idx+2)), (time[idx+2]+minSUPW(idx+3)))
    return memo[idx]

def minSUPWtab():
    global time, n

    dp = [0 for i in range(n)]
    dp[0] = time[0]
    dp[1] = time[1]
    dp[2] = time[2]

    for i in range(3,n):
        dp[i] = min(dp[i-1],dp[i-2],dp[i-3]) + time[i]

    return min(dp[n-1],dp[n-2],dp[n-3])


if __name__ == "__main__":
    n = 10
    count = 0
    memo = [-1 for i in range(n+1)]
    time = [3,2,1,1,2,3,1,3,2,1]
    
    if n < 4:
        print(min(time))
    print(minSUPW(0))
    print(minSUPWtab())
    # print(count)


    n = 5
    memo = [-1 for i in range(n+1)]
    time = [2,2,3,2,2]

    if n < 4:
        print(min(time))
    print(minSUPW(0))
    print(minSUPWtab())


    n = 8
    memo = [-1 for i in range(n+1)]
    time = [3,2,3,2,3,5,1,3]

    if n < 4:
        print(min(time))
    print(minSUPW(0))
    print(minSUPWtab())