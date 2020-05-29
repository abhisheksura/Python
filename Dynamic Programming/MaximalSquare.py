"""
    LeetCode #221 - Maximal Square
    https://leetcode.com/problems/maximal-square/
    
    Time Complexity - O(NxN)
    Space Complexity - O(NxN)
    Dynamic Programming - Bottom Up Approach
"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        
        max_size = 0
        
        row = len(matrix)
        col = len(matrix[0])
        
        # Creating the new 2D List with row+1 rows and col+1 columns and filling it up with 0
        dp = [[0] * (col+1) for _ in range(row+1)]
        
        for i in range(1, row+1):
            for j in range(1, col+1):
                # if matrix is 0 then it will be 0, if it is 1 then take the min of other 3 sides of matrix
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
                    max_size = max(max_size, dp[i][j])                

        return max_size * max_size
