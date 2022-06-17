# https://codeforces.com/problemset/problem/1061/C


def countMultiplicity(idx,nidx):
    global nums
    
    # base case
    if nidx >= n or idx > n:
        return 0

    cnt = 0
    if nums[nidx]%idx == 0:
        cnt = 1 + countMultiplicity(idx+1,nidx+1)
    cnt += countMultiplicity(idx,nidx+1)
        
    return cnt

def countMultiplicityTab():
    global nums

    dp = [[0 for i in range(n)] for j in range(n)]

    dp[0][0] = 1
    for c in range(1,n):
        dp[0][c] = 1+dp[0][c-1]
    
    for r in range(1,n):
        pos = r+1
        for c in range(n):
            if c < r:
                dp[r][c] = dp[r-1][c]
            elif nums[c]%pos == 0:
                dp[r][c] = dp[r-1][c] - dp[r-1][c-1] + dp[r-1][c-1] + dp[r][c-1]
            else:
                dp[r][c] = dp[r-1][c] - dp[r-1][c-1] + dp[r][c-1]

    # print(dp)
    return dp[n-1][n-1]

def countMultiplicityTab1():
    global nums

    dp = [[0 for i in range(n)] for j in range(2)]

    dp[0][0] = 1
    for c in range(1,n):
        dp[0][c] = 1+dp[0][c-1]
    
    for r in range(1,n):
        pos = r+1
        for c in range(n):
            if c < r:
                dp[1][c] = dp[0][c]
            elif nums[c]%pos == 0:
                dp[1][c] = dp[0][c] - dp[0][c-1] + dp[0][c-1] + dp[1][c-1]
            else:
                dp[1][c] = dp[0][c] - dp[0][c-1] + dp[1][c-1]
        for c in range(n):
            dp[0][c] = dp[1][c]

    # print(dp)
    return dp[1][n-1]


if __name__== "__main__":
    nums = [2, 2, 1, 22, 14]
    n = len(nums)
    print("Top Down","Array",nums,"Count",countMultiplicity(1,0))
    print("Bottom Up","Array",nums,"Count",countMultiplicityTab())
    print("Bottom Up1","Array",nums,"Count",countMultiplicityTab1())

    nums = [2, 2, 1]
    n = len(nums)
    print("Top Down","Array",nums,"Count",countMultiplicity(1,0))
    print("Bottom Up","Array",nums,"Count",countMultiplicityTab())
    print("Bottom Up1","Array",nums,"Count",countMultiplicityTab1())

    nums = [2, 2, 1,22]
    n = len(nums)
    print("Top Down","Array",nums,"Count",countMultiplicity(1,0))
    print("Bottom Up","Array",nums,"Count",countMultiplicityTab())
    print("Bottom Up1","Array",nums,"Count",countMultiplicityTab1())

    nums = [1,2]
    n = len(nums)
    print("Top Down","Array",nums,"Count",countMultiplicity(1,0))
    print("Bottom Up","Array",nums,"Count",countMultiplicityTab())
    print("Bottom Up1","Array",nums,"Count",countMultiplicityTab1())