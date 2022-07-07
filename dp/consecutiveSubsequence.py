# https://codeforces.com/problemset/problem/977/F
# Consecutive Subsequence
# You are given an integer array of length n.

# You have to choose some subsequence of this array of maximum length such that this subsequence forms a 
# increasing sequence of consecutive integers. In other words the required sequence should be equal to [x,x+1,…,x+k−1] 
# for some value x and length k.

# Input
# The first line of the input containing integer number n (1≤n≤2⋅105) — the length of the array. 
# The second line of the input containing n integer numbers a1,a2,…,an (1≤ai≤109) — the array itself.

# Output
# On the first line print k — the maximum length of the subsequence of the given array that forms an 
# increasing sequence of consecutive integers.

# On the second line print the sequence of the indices of the any maximum length subsequence of the given 
# array that forms an increasing sequence of consecutive integers.

# Examples

# Input - 7, 3 3 4 7 5 6 8
# Output -  4, 2 3 5 6  [These are indexes in the o/p, not the values]
# All valid answers for the first example (as sequences of indices):
# [1,3,5,6]
# [2,3,5,6]
# Input - 6, 1 3 5 2 4 6
# Output - 2, 1 4 
# [1,4]
# [2,5]
# [3,6]
# Input - 4, 10 9 8 7
# Output - 1, 1 
# [1]
# [2]
# [3]
# [4]
# Input - 9, 6 7 8 3 4 5 9 10 11
# Output - 6, 1 2 3 7 8 9 
# [1,2,3,7,8,9]

import copy
def maxConsecutiveSubsequence(op,idx):
    global n, nums, fop
    # print(op,idx)

    # Base case
    if idx > n-1:
        return

    if len(op) > 0:
        # consider it
        if nums[op[-1]] + 1 == nums[idx]:
            op.append(idx)
    else:
        op.append(idx)
    # Move to next
    maxConsecutiveSubsequence(op,idx+1)
    if len(fop) < len(op):
        fop = copy.deepcopy(op)
    return fop

def maxConsecutiveSubsequence2(prev,next):
    if next == n:
        return 0

    if (prev,next) in memo:
        return memo[prev,next]
    ans = 0
    if nums[prev]+1 == nums[next]:
        ans = max(ans,1 + maxConsecutiveSubsequence2(next,next+1))
    else:
        ans = max(ans, maxConsecutiveSubsequence2(prev,next+1))

    memo[prev,next] = ans
    return ans


# Using 2 D Array, Bottom Up
def maxConsecutiveSubsequenceTab():
    global n, nums
    dp = [[0 for i in range(n)] for j in range(n)]

    max_r = 0
    max_cnt = 0
    for r in range(n):
        cnt = 0
        for c in range(r,n):
            if c == r:
                dp[r][c] = 1
                next = nums[c]+1
                cnt += 1
            else:
                if nums[c] == next:
                    dp[r][c] = 1
                    next += 1
                    cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
            max_r = r

    # for e in dp:
    #     print(e)

    op = []
    for i in range(n):
        if dp[max_r][i] == 1:
            op.append(i)
    # print(dp[max_r],op,max_cnt)
    return op,max_cnt

# Using 1 D Array, Bottom Up
def maxConsecutiveSubsequenceTab2():
    global n, nums
    dp = [0 for i in range(n)]

    max_cnt = 0
    ans = []
    for r in range(n):
        cnt = 0
        for c in range(n):
            if c < r:
                dp[c] = 0
            elif c == r:
                dp[c] = 1
                next = nums[c]+1
                cnt += 1
            else:
                if nums[c] == next:
                    dp[c] = 1
                    next += 1
                    cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
            ans = copy.deepcopy(dp)
    op = []
    for i in range(n):
        if ans[i] == 1:
            op.append(i)
    return op,max_cnt


def maxConsecutiveSubsequenceTab3():
    dp = {}
    maxcnt = ([],0)
    for i in range(n):
        if nums[i]-1 in dp:
            dp[nums[i]] = (dp[nums[i]-1][0]+[i],dp[nums[i]-1][1] + 1)
        else:
            dp[nums[i]] = ([i],1)
        if maxcnt[1] < dp[nums[i]][1]:
            maxcnt = dp[nums[i]]

    return maxcnt

    

if __name__ == "__main__":

    nums = [3, 3, 4, 7, 5, 6, 8]    
    n = len(nums)
    fop = []
    print("Top Down",maxConsecutiveSubsequence([],0),len(fop))
    memo = {}
    print("Top Down2",1+maxConsecutiveSubsequence2(0,1))
    print("Bottom Up1",maxConsecutiveSubsequenceTab())
    print("Bottom Up2",maxConsecutiveSubsequenceTab2())
    print("Bottom Up3",maxConsecutiveSubsequenceTab3())
    

    nums = [1, 3, 5, 2, 4, 6]
    n = len(nums)
    fop = []
    print("Top Down",maxConsecutiveSubsequence([],0),len(fop))
    memo = {}
    print("Top Down2",1+maxConsecutiveSubsequence2(0,1))
    print("Bottom Up1",maxConsecutiveSubsequenceTab())
    print("Bottom Up2",maxConsecutiveSubsequenceTab2())
    print("Bottom Up3",maxConsecutiveSubsequenceTab3())

    nums = [10, 9, 8, 7]
    n = len(nums)
    fop = []
    print("Top Down",maxConsecutiveSubsequence([],0),len(fop))
    memo = {}
    print("Top Down2",1+maxConsecutiveSubsequence2(0,1))
    print("Bottom Up1",maxConsecutiveSubsequenceTab())
    print("Bottom Up2",maxConsecutiveSubsequenceTab2())
    print("Bottom Up3",maxConsecutiveSubsequenceTab3())

    nums = [6, 7, 8, 3, 4, 5, 9, 10, 11]
    n = len(nums)
    fop = []
    print("Top Down",maxConsecutiveSubsequence([],0),len(fop))
    memo = {}
    print("Top Down2",1+maxConsecutiveSubsequence2(0,1))
    print("Bottom Up1",maxConsecutiveSubsequenceTab())
    print("Bottom Up2",maxConsecutiveSubsequenceTab2())
    print("Bottom Up3",maxConsecutiveSubsequenceTab3())

