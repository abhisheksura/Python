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
    
"""
    LeetCode #100 - Same Tree
    https://leetcode.com/problems/same-tree/
    
    TC - O(N) No of nodes
    SC - O(logN) Best case & O(N) Worst Case unbalanced tree to keep recursion stack
"""
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        
        if (p and q is None) or (p is None and q):
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
