# Arrays with two pointer technique

# LeetCode #11 - Max area of the container
"""
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""
def maxArea(self, height: List[int]) -> int:
    max_area = 0
    l, r = 0, len(height) -1
    while l < r:
        max_area = max(max_area, min(height[l], height[r]) * (r-l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
        print("L: ", l, ", R: ", r, " === ", max_area)

    return max_area
    
    
# LeetCode #26 - Remove Duplicates from Sorted Array
"""
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

Given nums = [0,0,1,1,1,2,2,3,3,4],
Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
It doesn't matter what values are set beyond the returned length.
"""
def removeDuplicates(self, nums: List[int]) -> int:
    index = 0
    data = []
    for i in range(len(nums)):
        if nums[index] != nums[i] :
            index += 1
            nums[index] = nums[i]
    return index+1
    

# LeetCode #27 - Remove Element
"""
Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five 
of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
"""
def removeElement(self, nums: List[int], val: int) -> int:
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    return index
    
    
# LeetCode #80 - Remove Duplicates from Sorted Array II
"""
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.
"""
def removeDuplicates(self, nums: List[int]) -> int:
    index = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[index-1] or nums[i] != nums[index-2]:
            nums[index] = nums[i]
            index += 1
    return index
    
    
# LeetCode #283 - Move Zeroes
"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
"""
def moveZeroes(self, nums: List[int]) -> None:
    index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index], nums[i] = nums[i], nums[index]
            index += 1
    return index
    
    
# LeetCode #287 - Find the Duplicate Number
"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2

Example 2:

Input: [3,1,3,4,2]
Output: 3
"""
# Using Sorting - TC - O(nlogN) & SC - O(1) or O(N) to store the copy of array as it is readable
def findDuplicate(self, nums: List[int]) -> int:
    nums.sort()
    for i in range(len(nums)):
        if nums[i] == nums[i-1]:                
            return nums[i]
    return -1

# Using set TC - O(n) and SC - O(n) to store the elements in set
def findDuplicate(self, nums: List[int]) -> int:
    hash_set = set()
    for i in range(len(nums)):
        if nums[i] not in hash_set:                
            hash_set.add(nums[i])
        else:
            return nums[i]
    return -1
    
    
# LeetCode #344 - Reverse String
def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    for i in range(len(s)//2):
        s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]

    return s
