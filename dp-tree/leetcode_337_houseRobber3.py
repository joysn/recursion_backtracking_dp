# https://leetcode.com/problems/house-robber-iii/
# 337. House Robber III

# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

# Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

# Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

# Example 1:
# Input: root = [3,2,3,null,3,null,1]
# Output: 7
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

# Example 2:
# Input: root = [3,4,5,1,3,null,1]
# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

# [3,4,5,1,3,null,1]


# Runtime: 64 ms, faster than 76.14% of Python3 online submissions for House Robber III.
# Memory Usage: 18.5 MB, less than 8.24% of Python3 online submissions for House Robber III.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    gr = {}
    maxVal = -1*(sys.maxsize-1)
    
    
    def dfs(self,cur):
        if cur.left:
            self.dfs(cur.left)
        if cur.right:
            self.dfs(cur.right)
            
        rob = cur.val
        notRob = 0
        if cur.left:
            notRob += max(self.gr[cur.left][1],self.gr[cur.left][0])
            rob += self.gr[cur.left][0]
        if cur.right:
            notRob += max(self.gr[cur.right][1],self.gr[cur.right][0])
            rob += self.gr[cur.right][0]
        
        self.gr[cur] = [notRob,rob]
        
    
    def rob(self, root: Optional[TreeNode]) -> int:
        
        self.dfs(root)
        # print(self.gr)
        return max(self.gr[root][0],self.gr[root][1])
