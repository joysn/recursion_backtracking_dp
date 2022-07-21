# https://leetcode.com/problems/pascals-triangle/
# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:
# Input: numRows = 1
# Output: [[1]]

# Runtime: 44 ms, faster than 60.68% of Python3 online submissions for Pascal's Triangle.
# Memory Usage: 14 MB, less than 17.88% of Python3 online submissions for Pascal's Triangle.

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        op = []
        def pascalTriangle(r):
            if r == 1:
                op.append([1])
                return op
            
            if r == 2:
                op.append([1])
                op.append([1,1])
                return op
            
            pascalTriangle(r-1)
            top = [1]
            # print(op,op[-1],r)
            for i in range(1,r-1):
                # print(i)
                top.append(op[-1][i-1]+op[-1][i])
            top.append(1)
            op.append(top)
            return op
            
        return pascalTriangle(numRows)
        
        