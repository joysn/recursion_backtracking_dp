# https://leetcode.com/problems/interleaving-string/
# 97. Interleaving String

# Runtime: 62 ms, faster than 63.85% of Python3 online submissions for Interleaving String.
# Memory Usage: 15.7 MB, less than 18.73% of Python3 online submissions for Interleaving String.

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        def ifPossible(i,j,k):
            
            if k == len(s3):
                return True
            
            if (i,j,k) in cache:
                return cache[(i,j,k)]
            ans = False
            if i < len(s1) and s1[i] == s3[k]:
                ans |= ifPossible(i+1,j,k+1)
            if j < len(s2) and s2[j] == s3[k]:
                ans |= ifPossible(i,j+1,k+1)
                
            cache[(i,j,k)] = ans
            return ans
            
            
        cache = {}
        if len(s1) + len(s2) != len(s3):
            return False
        return ifPossible(0,0,0)