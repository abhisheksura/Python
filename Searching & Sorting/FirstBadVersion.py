"""
    LeetCode #278 - First Bad Version
    https://leetcode.com/problems/first-bad-version/
    
    Time Complexity - O(log N) Binary Search
    Space Complexity - O(1)
"""

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        while start <= end:
            mid = (start + end) // 2
            current_version = isBadVersion(mid)
            if current_version == False:
                start = mid + 1
            elif current_version == True:
                end = mid - 1
        return start
