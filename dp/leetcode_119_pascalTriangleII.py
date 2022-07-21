# https://leetcode.com/problems/pascals-triangle-ii/
# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]

# Example 2:
# Input: rowIndex = 0
# Output: [1]

# Example 3:
# Input: rowIndex = 1
# Output: [1,1]

# Runtime: 55 ms, faster than 31.00% of Python3 online submissions for Pascal's Triangle II.
# Memory Usage: 13.9 MB, less than 16.36% of Python3 online submissions for Pascal's Triangle II.

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        
        def pascalTriangle(r):
            # print(r)
            if r == 0:
                return [1]
            if r == 1:
                return [1,1]
            
            prevOp = pascalTriangle(r-1)
            currOp = [1]
            for i in range(1,r):
                currOp.append(prevOp[i-1]+prevOp[i])
            currOp.append(1)
            
            # print("Returning",r,currOp)
            return currOp
        
        
        return pascalTriangle(rowIndex)
        