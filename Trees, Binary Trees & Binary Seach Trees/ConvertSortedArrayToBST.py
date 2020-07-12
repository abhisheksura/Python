"""
    LeetCode #108 - Convert Sorted Array to Binary Search Tree
    https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
    
    # Use the binary search concept as it is sorted, middle element will be root
    # & its left elements will become left subtree & right elements will become right subtree.
    # Call this recursively for its childs.
"""
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0: return
        return self.construct_tree_from_array(nums, 0, len(nums)-1)
    
    def construct_tree_from_array(self, nums, left, right):
        if left > right: return
        
        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = self.construct_tree_from_array(nums, left, mid-1)
        node.right = self.construct_tree_from_array(nums, mid+1, right)
        return node
