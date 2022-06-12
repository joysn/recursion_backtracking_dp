# https://leetcode.com/problems/palindrome-partitioning/
# 131. Palindrome Partitioning
# Given a string s, partition s such that every substring of the partition is a palindrome. 
# Return all possible palindrome partitioning of s.

# A palindrome string is a string that reads the same backward as forward.

# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:
# Input: s = "a"
# Output: [["a"]]

import copy


class Solution:
    str = ""
    output = []
    memo = [[[]]]
    
    def isPalindrome(self,str):
        revStr = str[::-1]
        if str == revStr:
            return True
        return False

    def dp(self,idx):
        if idx == len(self.str):
            return [[]]
        
        ans = []
        res = [[]]
        if idx > len(self.memo):
            return self.memo[idx]
        for i in range(idx, len(self.str)):
            pstr = self.str[idx:i+1]
            if self.isPalindrome(pstr):
                res = self.dp(i+1)
                for e in res:
                    pstr_copy = copy.deepcopy(pstr)
                    e.insert(0,pstr_copy)
                for e in res:
                    ans.append(e)

        self.memo[idx] = copy.deepcopy(ans)
        return self.memo[idx]
                


    def partition(self, s: str):
        self.str = s
        self.memo = [[[]] for i in range(len(self.str))]
        return self.dp(0)



if __name__ == "__main__":
    
    inputs = ["aab","a","aba","aaba","aaaa","aaaaa"]
    for str in inputs:
        s = Solution()
        print(s.partition(str))
    # print(s[0:1])
    # print(s[0:3])


