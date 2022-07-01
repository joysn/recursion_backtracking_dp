# https://leetcode.com/problems/palindrome-partitioning-iv/
# 1745. Palindrome Partitioning IV
# Given a string s, return true if it is possible to split the string s into three non-empty palindromic substrings. 
# Otherwise, return false.​​​​​

# A string is said to be palindrome if it the same string when reversed.

# Example 1:
# Input: s = "abcbdd"
# Output: true
# Explanation: "abcbdd" = "a" + "bcb" + "dd", and all three substrings are palindromes.

# Example 2:
# Input: s = "bcbddxy"
# Output: false
# Explanation: s cannot be split into 3 palindromes.

def isPalindrome(s):
    return s == s[::-1]

def isPalindrome3Cut(idx,cuts_left):

    if idx == n:
        if cuts_left == 0:
            return True
        else:
            return False
    if cuts_left < 0:
        return False

    if memo[idx][cuts_left] != -1:
        return memo[idx][cuts_left]
    ans = False
    for j in range(idx,n):
        if isPalindrome(s[idx:j+1]):
            ans |= isPalindrome3Cut(j+1,cuts_left-1)
            if ans == True:
                break
    memo[idx][cuts_left] = ans
    return ans


# Runtime: 4141 ms, faster than 74.29% of Python3 online submissions for Palindrome Partitioning IV.
# Memory Usage: 45.6 MB, less than 38.57% of Python3 online submissions for Palindrome Partitioning IV.

def isPalindrome3CutTab():
    is_pal = [[False]*n for i in range(n)]

    for i in range(n-1,-1,-1):
        for j in range(i,n):
            is_pal[i][j] =  s[i] == s[j] and\
                (i-j<=1 or is_pal[i+1][j-1])

    for start3 in range(n-1,1,-1):
        if not is_pal[start3][n-1]:
            continue
        for start2 in range(start3-1,0,-1):
            if is_pal[start2][start3-1] and is_pal[0][start2-1]:
                return True
    return False

if __name__=="__main__":
    ss = ["abcbdd","bcbddxy","abc","aba","abcd","aaaa","bbaac"]
    for s in ss:
        n = len(s)
        memo = [[-1 for i in range(4)] for j in range(n)]
        print("String",s,isPalindrome3Cut(0,3))
        print("String",s,isPalindrome3CutTab())