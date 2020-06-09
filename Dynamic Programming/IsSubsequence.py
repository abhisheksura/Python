"""
    LeetCode #392 - Is Subsequence
    https://leetcode.com/problems/is-subsequence/
    
    Time Complexity - O(SxT)
    Space Complexity - O(SxT)
    Dynamic Programming - Bottom Up Approach
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        row = len(s)
        col = len(t)

        dp = [[0] * (col+1) for _ in range(row+1)]

        for i in range(1, row+1):
            for j in range(1, col+1):
                if s[i-1]== t[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]

        return True if dp[-1][-1] == len(s) else False
