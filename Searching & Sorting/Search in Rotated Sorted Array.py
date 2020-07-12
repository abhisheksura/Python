"""
    LeetCode #33 - Search in Rotated Sorted Array
    https://leetcode.com/problems/search-in-rotated-sorted-array/

    # First search the pivot(the starting element of sorted array)
    # if the target element is greater than pivot & its right most element then do the binary search from the pivot/second part
    # else ignore the right part and implement BS on left part.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        left, right = 0, len(nums)-1

        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid
              
        start = left
        left, right = 0, len(nums)-1

        if target >= nums[start] and target <= nums[right]:
            left = start
        else:
            right = start
            
        while left <= right:
            mid = (left+right)//2
            
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid+1
            else:
                right = mid-1
                
        return -1
