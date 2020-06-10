"""
Time Comlexity - O(log N)
"""
class Solution:
    # Iterative Approach
    # Space Complexity - O(1)
    def binarySearch(self, nums: List[int], target: int) -> int:
        
        start, end = 0, len(nums)

        while start <= end:
            mid = (start+end)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid+1
            else:
                end = mid - 1
        return -1;

    # recursive
    # Space Complexity - O(log N) call stack space
    def binaryRecursiveSearch(self, nums: List[int], target: int, start, end) -> int:
        
        if start <= end:
            mid = (start+end)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return self.binaryRecursiveSearch(nums, target, mid+1, end)
            else:
                return self.binaryRecursiveSearch(nums, target, start, mid-1)

        return -1;
