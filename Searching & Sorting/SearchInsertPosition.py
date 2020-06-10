"""
    LeetCode #35 - Search Insert Position
    https://leetcode.com/problems/search-insert-position/
    
    Time Complexity - O(log N) No of Nodes in Tree
    Space Complexity - O(1)
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if target > nums[len(nums)-1]:
            return len(nums)
        
        start, end = 0, len(nums)
        
        while start <= end:
            mid = (start+end)//2
            
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return start
