"""
    LeetCode #647 - Palindromic Substrings
    https://leetcode.com/problems/palindromic-substrings/
    
    LeetCode #5 - Longest Palindromic Substring
    https://leetcode.com/problems/longest-palindromic-substring/
    
    LeetCode #516 - Longest Palindromic Subsequence
    https://leetcode.com/problems/longest-palindromic-subsequence/
    
    Time Complexity - O(NxN)
    Space Complexity - O(NxN)
    Dynamic Programming - Bottom Up Approach
"""

class Solution:
    # Palindromic Strings (bbbab = > 7 = > {b, b, b, bb, bb, bbb, bab})
    def countSubstrings(self, s: str) -> int:
        count = 0
        dp = [[0] * len(s) for _ in range(len(s))]
        
        # each string is a palindrome
        for i in range(len(s)):
            dp[i][i] = 1
            count += 1
            
        # for each string, start by length 1 till the end of the string
        for l in range(1, len(s)):
            for i in range(len(s)-l):
                j = i+l
                
                # if the length of the string is 2
                if s[i] == s[j] and i == j-1:
                    dp[i][j] = 1
                    count += 1
                    
                # if the length of the string is greater than 2
                elif s[i] == s[j] and dp[i+1][j-1] == 1:
                    dp[i][j] = 1
                    count += 1
        return count

    # Longest Palindromic Substring (bbbab = > 3 => (bbb or bab))
    def longestPalindrome(self, s: str) -> str:
        dp = [[0] * len(s) for _ in range(len(s))]
        start, end = 0, 0 # To track the first and last index of longest palindrome
        
        for i in range(len(s)):
            dp[i][i] = 1
            
        for l in range(1, len(s)):
            for i in range(len(s)-l):
                j = i+l

                # if the length of the string is 2
                if s[i] == s[j] and i == j-1:
                    dp[i][j] = 2
                    start, end = i, j
                    
                # if the length of the string is greater than 2
                elif s[i] == s[j] and dp[i+1][j-1] != 0:
                    dp[i][j] = 2 + dp[i+1][j-1]
                    start, end = i, j
        return s[start:end+1]

    # Longest Palindromic subsequence (bbbab = > 4 => bbbb)
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        
        for i in range(len(s)):
            dp[i][i] = 1
        
        for l in range(1, len(s)):
            for i in range(len(s)-l):
                j = i+l

                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        return dp[0][-1]
