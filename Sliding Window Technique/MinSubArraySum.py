"""
    LeetCode #209 - Minimum Size Subarray Sum
    https://leetcode.com/problems/minimum-size-subarray-sum/
    
    Time Complexity - O(N)
    Space Complexity - O(1)
    Sliding Window & 2 Pointer Technique
"""

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        current_sum, slow = 0, 0
        min_count = float('inf')

        for fast in range(len(nums)):
            current_sum += nums[fast]
            while current_sum >= s:
                min_count = min(min_count, fast-slow+1)
                current_sum -= nums[slow]
                slow += 1
                
        return min_count if min_count != float('inf') else 0
