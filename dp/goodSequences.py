# Good Sequences
# https://codeforces.com/problemset/problem/264/B#:~:text=A%20sequence%20x%201%2C%20x,i%20%E2%89%A4%20k%20%2D%201).

# B. Good Sequences
# time limit per test2 seconds
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# Squirrel Liss is interested in sequences. She also has preferences of integers. She thinks n integers a1, a2, ..., an are good.

# Now she is interested in good sequences. A sequence x1, x2, ..., xk is called good if it satisfies the following three conditions:

# The sequence is strictly increasing, i.e. xi < xi + 1 for each i (1 ≤ i ≤ k - 1).
# No two adjacent elements are coprime, i.e. gcd(xi, xi + 1) > 1 for each i (1 ≤ i ≤ k - 1) (where gcd(p, q) denotes the 
# greatest common divisor of the integers p and q).
# All elements of the sequence are good integers.
# Find the length of the longest good sequence.

# Input
# The input consists of two lines. The first line contains a single integer n (1 ≤ n ≤ 105) — the number of good integers. The second line contains a single-space separated list of good integers a1, a2, ..., an in strictly increasing order (1 ≤ ai ≤ 105; ai < ai + 1).

# Output
# Print a single integer — the length of the longest good sequence.

# 2 3 4 6 9
# op - 4

# 1 2 3 5 6 7 8 9 10
# op - 4

import math
def isCoPrime(a,b):
    hcf = 1
    big = max(a,b)
    for i in range(2,big+1):
        if a%i == 0 and b%i == 0:
            hcf = i
            break
    return hcf == 1

#O(n*n)
def maxGoodSeq(idx):
    if idx == n-1:
        return 1

    if idx in memo:
        return memo[idx]
    maxcnt = 1
    for i in range(idx+1,n):
        if not isCoPrime(nums[idx],nums[i]):
            maxcnt = max(maxcnt, 1+ maxGoodSeq(i))
        else:
            maxcnt = max(maxcnt, maxGoodSeq(i))

    memo[idx] = maxcnt
    return maxcnt

#O(n*n)
def maxGoodSeqTab():
    dp = [1 for i in range(n)]

    maxcnt = 0
    for i in range(1,n):
        for j in range(0,i):
            if not isCoPrime(nums[i],nums[j]):
                dp[i] = max(dp[i],1+dp[j])
                maxcnt = dp[i]
    return maxcnt


# New method
def getPrimeDivisors(n):
    op = []
    for i in range(2,math.ceil(math.sqrt(n))+1):
        if n%i == 0:
            op.append(i)
            while (n%i == 0):
                n //= i
    # If n has prime divisors, it will get divided and reach 1
    # If n is a prime number, it will remain at n (>1)
    if n > 1 :
        op.append(n)
    return op
        
def maxGoodSeqTab2():
    dp_prime = [0 for i in range(1000)]
    ans = 0
    for i in range(n):
        pd = getPrimeDivisors(nums[i])
        best_ending = 0
        for prime in pd:
            best_ending = max(best_ending,dp_prime[prime])

        for prime in pd:
            dp_prime[prime] = best_ending + 1
            ans = max(ans,dp_prime[prime])

    return ans


if __name__=="__main__":
    nums = [2, 3, 4, 6, 9]
    n = len(nums)
    memo = {}
    print("Top Down",maxGoodSeq(0))
    print("Bottom Up",maxGoodSeqTab())
    print("Optimized Bottom Up",maxGoodSeqTab2())
    # print(getPrimeDivisors(4))
    

    nums = [1, 2, 3, 5, 6, 7, 8, 9, 10]
    n = len(nums)
    memo = {}
    print("Top Down",maxGoodSeq(0))
    print("Bottom Up",maxGoodSeqTab())
    print("Optimized Bottom Up",maxGoodSeqTab2())