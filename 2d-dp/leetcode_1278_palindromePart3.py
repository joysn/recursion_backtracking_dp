# https://leetcode.com/problems/palindrome-partitioning-iii/
# 1278. Palindrome Partitioning III

# You are given a string s containing lowercase letters and an integer k. You need to :

# First, change some characters of s to other lowercase English letters.
# Then divide s into k non-empty disjoint substrings such that each substring is a palindrome.
# Return the minimal number of characters that you need to change to divide the string.
 

# Example 1:
# Input: s = "abc", k = 2
# Output: 1
# Explanation: You can split the string into "ab" and "c", and change 1 character in "ab" to make it palindrome.

# Example 2:
# Input: s = "aabbc", k = 3
# Output: 0
# Explanation: You can split the string into "aa", "bb" and "c", all of them are palindrome.

# Example 3:
# Input: s = "leetcode", k = 8
# Output: 0

# Runtime: 489 ms, faster than 38.77% of Python3 online submissions for Palindrome Partitioning III.
# Memory Usage: 14.5 MB, less than 56.46% of Python3 online submissions for Palindrome Partitioning III.

import sys
def numChanges(s):
    lo,hi = 0,len(s)-1
    count = 0
    while lo < hi:
        if s[lo] != s[hi]:
            count += 1
        lo += 1
        hi -= 1
    return count


def minUpdates(idx,curr_k):
    if (idx,curr_k) not in memo:
        if curr_k == 1:
            memo[idx,curr_k] = numChanges(s[:idx+1])
        else:
            ans = sys.maxsize
            for j in range(curr_k-2,idx):
                ans = min ( ans, minUpdates(j,curr_k-1)+numChanges(s[j+1:idx+1]))
            memo[idx,curr_k] = ans
    return memo[idx,curr_k]
    



if __name__ == "__main__":
    s = "abc"
    k = 2
    n = len(s)
    memo = dict()
    print("Min updates required for string",s,"to have subsets",k,"is",minUpdates(n-1,k))