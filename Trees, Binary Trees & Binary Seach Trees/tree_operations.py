"""
    LeetCode #226 - Invert Binary Tree
    https://leetcode.com/problems/longest-common-subsequence/
    
    Time Complexity - O(N) No of Nodes in Tree
    Space Complexity - O(log N) Average Case & O(N) Worst case if tree is skewed we have to store all the elements in recursion stack
"""

class Binary Tree:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        
        root.left, root.right = root.right, root.left
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
            
        return root
