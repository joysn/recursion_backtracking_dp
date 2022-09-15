# https://leetcode.com/problems/shortest-common-supersequence/
# 1092. Shortest Common Supersequence
# Runtime: 2274 ms, faster than 5.04% of Python3 online submissions for Shortest Common Supersequence .
# Memory Usage: 154.5 MB, less than 5.29% of Python3 online submissions for Shortest Common Supersequence .

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        def lcs(i,j):
            
            if i == len(str1) or j == len(str2):
                return ""
            
            if (i,j) in cache:
                return cache[(i,j)]
            ans = ""
            if str1[i] == str2[j]:
                tans = str1[i] + lcs(i+1,j+1) 
                if len(tans) > len(ans):
                    ans = tans
            tans = lcs(i+1,j)
            if len(tans) > len(ans):
                ans = tans
            tans = lcs(i,j+1)
            if len(tans) > len(ans):
                ans = tans
              
            cache[(i,j)] = ans
            return ans
        
        
        cache = {}
        op = lcs(0,0)
        # print(op)
        
        i,j = 0,0
        res = ""
        for ch in op:
            while i< len(str1) and ch != str1[i]:
                res += str1[i]
                i += 1
            while j < len(str2) and ch != str2[j]:
                res += str2[j]
                j += 1
                
            res += ch
            i += 1
            j += 1
            
        return res+str1[i:]+str2[j:]
            
        