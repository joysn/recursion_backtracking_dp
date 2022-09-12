# https://leetcode.com/problems/palindromic-substrings/
# 647. Palindromic Substrings

# Runtime: 1937 ms, faster than 5.02% of Python3 online submissions for Palindromic Substrings.
# Memory Usage: 179.3 MB, less than 5.32% of Python3 online submissions for Palindromic Substrings.

class Solution:
    def countSubstrings(self, s: str) -> int:
            
        def isPalindrome(st,en):
            if st == len(s) or en < 0:
                return False
            if st == en:
                return True
            
            if st+1 == en:
                if s[st] == s[en]:
                    return True
                else:
                    return False
                
            if (st,en) in cache:
                return cache[(st,en)]
            if s[st] == s[en] and isPalindrome(st+1,en-1):
                cache[(st,en)] = True
                return True
            
            cache[(st,en)] = False
            return False
        
        
        ans = 0
        cache = {}
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                if isPalindrome(i,j):
                    ans += 1
        return ans
            
        