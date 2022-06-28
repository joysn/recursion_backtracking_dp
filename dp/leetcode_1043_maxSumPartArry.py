# https://leetcode.com/problems/partition-array-for-maximum-sum/
# 1043. Partition Array for Maximum Sum

# Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

# Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

# Example 1:
# Input: arr = [1,15,7,9,2,5,10], k = 3
# Output: 84
# Explanation: arr becomes [15,15,15,9,10,10,10]

# Example 2:
# Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
# Output: 83

# Example 3:
# Input: arr = [1], k = 1
# Output: 1

# Runtime: 4945 ms, faster than 5.17% of Python3 online submissions for Partition Array for Maximum Sum.
# Memory Usage: 17.3 MB, less than 5.73% of Python3 online submissions for Partition Array for Maximum Sum.

def maxSum(idx,curr_k):
    if curr_k > k:
        return 0
    if idx >= n:
        return 0
    
    if memo[idx][curr_k] != -1:
        return memo[idx][curr_k]
    # Partition
    ans = curr_k*max(arr[idx-curr_k+1:idx+1]) + maxSum(idx+1,1)
    # Do not partition
    ans = max(ans,maxSum(idx+1,curr_k+1))

    memo[idx][curr_k] = ans
    return ans


# Runtime: 4081 ms, faster than 6.88% of Python3 online submissions for Partition Array for Maximum Sum.
# Memory Usage: 14.5 MB, less than 25.38% of Python3 online submissions for Partition Array for Maximum Sum.
def maxSum2(idx):
    if idx >= n:
        return 0
    
    if memo[idx] != -1:
        return memo[idx]
    # Partition
    ans = -1
    for i in range(1,k+1):
        if idx+i <= n:
            ans = max(ans, i*max(arr[idx:idx+i]) + maxSum2(idx+i))
        
    memo[idx] = ans
    return ans

if __name__=="__main__":
    arr = [1,15,7,9,2,5,10]
    k = 3
    n = len(arr)
    memo = [[-1 for i in range(k+1)] for j in range(n)]
    print("Top Down",maxSum(0,1))
    memo = [-1 for i in range(n)]
    print("Top Down2",maxSum2(0))

    arr = [1,4,1,5,7,3,6,1,9,9,3]
    k = 4
    n = len(arr)
    memo = [[-1 for i in range(k+1)] for j in range(n)]
    print("Top Down",maxSum(0,1))
    memo = [-1 for i in range(n)]
    print("Top Down2",maxSum2(0))

    arr = [1]
    k = 1
    n = len(arr)
    memo = [[-1 for i in range(k+1)] for j in range(n)]
    print("Top Down",maxSum(0,1))
    memo = [-1 for i in range(n)]
    print("Top Down2",maxSum2(0))