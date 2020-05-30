"""
    LeetCode #1143 - Longest Common Subsequence
    https://leetcode.com/problems/longest-common-subsequence/
    
    Time Complexity - O(NxN)
    Space Complexity - O(NxN)
    Dynamic Programming - Bottom Up Approach
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]
        
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                
                # if the string matches then diagonal element + 1
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    
                # else max of adjacent element
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        # return the last element of the matrix        
        return dp[-1][-1]
