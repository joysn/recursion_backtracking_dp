https://leetcode.com/problems/maximize-palindrome-length-from-subsequences/
1771. Maximize Palindrome Length From Subsequences

Runtime: 9411 ms, faster than 7.32% of Python3 online submissions for Maximize Palindrome Length From Subsequences.
Memory Usage: 713 MB, less than 7.32% of Python3 online submissions for Maximize Palindrome Length From Subsequences.


class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        
        def maxPalSubseq(st,en,done):
            if not done and (st >= m or en < m):
                return 0
            if st > en:
                return 0
            if st == en:
                return 1
            
            if st+1 == en and final[st] == final[en]:
                return 2
            
            if (st,en,done) in cache:
                return cache[(st,en,done)]
            ans = 0
            if final[st] == final[en]:
                ans = 2 + maxPalSubseq(st+1,en-1,True)
            else:
                ans = max(ans, maxPalSubseq(st+1,en,done), maxPalSubseq(st,en-1,done))
            
            cache[(st,en,done)] = ans
            return ans
            
            
        
        final = word1+word2
        m = len(word1)
        cache = {}
        ans = maxPalSubseq(0,len(final)-1,False)
        return ans


        