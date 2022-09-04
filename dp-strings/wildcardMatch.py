# https://leetcode.com/problems/wildcard-matching/
# 44. Wildcard Matching
# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

# Example 1:
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

# Example 2:
# Input: s = "aa", p = "*"
# Output: true
# Explanation: '*' matches any sequence.

# Example 3:
# Input: s = "cb", p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

# Runtime: 1055 ms, faster than 49.84% of Python3 online submissions for Wildcard Matching.
# Memory Usage: 148.5 MB, less than 7.52% of Python3 online submissions for Wildcard Matching.

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def match(i,j):
            if i == len(s) and j == len(p):
                return True
            if j == len(p):
                return False
            
            if (i,j) in cache:
                return cache[(i,j)]
            ans = False
            if i < len(s) and s[i] == p[j]:
                ans |= match(i+1,j+1)
            elif  p[j] == "?":
                if i == len(s):
                    return False
                else:
                    ans |= match(i+1,j+1)
            elif p[j] == "*":
                if i < len(s):
                    ans |= match(i+1,j)
                ans |= match(i,j+1)
                
            cache[(i,j)] = ans
            return ans
            
        cache = {}
        return match(0,0)