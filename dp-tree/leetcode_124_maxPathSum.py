# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# 124. Binary Tree Maximum Path Sum
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any non-empty path.

# Example 1:
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

# Example 2:
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

# [5,4,8,11,null,13,4,7,2,null,null,null,1]
# [1,2,-3]
# [-3]

# Runtime: 157 ms, faster than 30.85% of Python3 online submissions for Binary Tree Maximum Path Sum.
# Memory Usage: 25.2 MB, less than 5.16% of Python3 online submissions for Binary Tree Maximum Path Sum.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    
    gr = {}
    ans = -1*(sys.maxsize-1)
    
    def dfs(self,cur):    
        if cur.left != None:
            self.dfs(cur.left)
        if cur.right != None:
            self.dfs(cur.right)
            
        self.gr[cur] = cur.val
        temp_val = cur.val
        if cur.left!= None and self.gr[cur.left] > 0:
            self.gr[cur] = max(self.gr[cur],cur.val+self.gr[cur.left])
            temp_val += self.gr[cur.left]
        if cur.right != None and self.gr[cur.right] > 0:
            self.gr[cur] = max(self.gr[cur],cur.val+self.gr[cur.right])
            temp_val += self.gr[cur.right]
            
        self.ans = max(self.ans,self.gr[cur])
        self.ans = max(self.ans,temp_val)
            
            
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        # print(self.gr)
        return self.ans
        