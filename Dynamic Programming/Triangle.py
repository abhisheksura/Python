"""
    LeetCode #120 - Triangle
    https://leetcode.com/problems/triangle/    
    Time Complexity - O(MxN) / O(rows x cols)
    Space Complexity - O(1) - We are modifying the existing list triangle - inplace
    Dynamic Programming - Bottom Up Approach
"""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if triangle is None:
            return
        
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                
                # sum 1st element of current row with 1st element of previous row
                if j == 0:
                    triangle[i][j] = triangle[i-1][j] + triangle[i][j]

                # sum the last element of current row with last element of previous row
                # as it is a triangle we are doing j-1 of previous row
                elif j == len(triangle[i])-1:
                    triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
                    
                # sum the current element with adjacent elements from previous row
                else:
                    triangle[i][j] = min(triangle[i-1][j], triangle[i-1][j-1]) + triangle[i][j]

        return min(triangle[-1])
