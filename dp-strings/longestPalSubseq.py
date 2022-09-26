# https://leetcode.com/problems/longest-palindromic-subsequence/
# 516. Longest Palindromic Subsequence

# Runtime: 3143 ms, faster than 45.05% of Python3 online submissions for Longest Palindromic Subsequence.
# Memory Usage: 249.8 MB, less than 12.16% of Python3 online submissions for Longest Palindromic Subsequence.

class Solution:
    
    def longestPalindromeSubseq(self, s: str) -> int:
        
        def countPalindromeSub(i,j):
            if i == j:
                return 1
            if i+1 == j and s[i] == s[j]:
                    return 2
            if (i,j) in cache:
                return cache[(i,j)]
            ans = 0
            if s[i] == s[j]:
                ans = max(ans,2 + countPalindromeSub(i+1,j-1))
            else:
                ans = max(ans, countPalindromeSub(i+1,j), countPalindromeSub(i,j-1))
                
            cache[(i,j)] = ans
            return ans
        
        ans = 0
        cache = {}
        return countPalindromeSub(0,len(s)-1)
