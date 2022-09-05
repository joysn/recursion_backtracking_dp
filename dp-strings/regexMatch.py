# Regular Expression Match
# 10. Regular Expression Matching
# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# Example 1:
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

# Example 2:
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

# Example 3:
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".

# Runtime: 82 ms, faster than 52.17% of Python3 online submissions for Regular Expression Matching.
# Memory Usage: 14.3 MB, less than 6.23% of Python3 online submissions for Regular Expression Matching.


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
            if p[j] == ".":
                if i < len(s):
                    ans |= match(i+1,j+1)
                else:
                    ans = False
            elif p[j] == "*":
                if j == 0: # First character
                    return False
                if i < len(s) and (s[i] == p[j-1] or p[j-1] == "."):
                    ans |= match(i+1,j)
                ans |= match(i,j+1)
            if j+1 < len(p) and p[j+1] == "*":
                ans |= match(i,j+2)
                
            cache[(i,j)] = ans
            return ans
        
        cache = {}
        return match(0,0)
        