# https://leetcode.com/problems/palindrome-partitioning-ii/
# 132. Palindrome Partitioning II
# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return the minimum cuts needed for a palindrome partitioning of s. 

# Example 1:
# Input: s = "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

# Example 2:
# Input: s = "a"
# Output: 0

# Example 3:
# Input: s = "ab"
# Output: 1
import sys

def isPalindrome(s):
    return s == s[::-1]


# Runtime: 4129 ms, faster than 19.58% of Python3 online submissions for Palindrome Partitioning II.
# Memory Usage: 16 MB, less than 69.46% of Python3 online submissions for Palindrome Partitioning II.

def countPart(idxs,idxe):
    if idxs == n:
        return sys.maxsize

    if memo[idxs][idxe] != -1:
        return memo[idxs][idxe]
    cnt = sys.maxsize
    if isPalindrome(s[idxs:idxe+1]):
        cnt = 0
    else:
        for i in range(idxs,idxe+1):
            if isPalindrome(s[idxs:i+1]):
                cnt = min(cnt,1+countPart(i+1,idxe))

    # print("idx",idx,"cnt",cnt)
    memo[idxs][idxe] = cnt
    return cnt
        


if __name__ == "__main__":
    ss = ["a","ab","aab","abb","abba","abbbc","abcbdd","bbab"]
    for s in ss:
        n = len(s)
        memo = [[-1 for i in range(n)] for j in range(n)]
        print("String",s,"Cut Count",countPart(0,n-1))