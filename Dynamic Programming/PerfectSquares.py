"""
    LeetCode #279 - Perfect Squares
    https://leetcode.com/problems/perfect-squares/
    
    Time Complexity - O(N√N)
    Space Complexity - O(N)
    Dynamic Programming - Bottom Up Approach
"""

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [float('inf')] * (n+1)
        
        for i in range(1, n+1):
            for j in range(1, n+1):
                k = i-j*j
                if k < 0:
                    break
                if j*j <= i:
                    dp[i] = min(dp[i], dp[i-j*j]+1)
                # print(i, j, i-j*j, dp[i])
        return dp[n]
