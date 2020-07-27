from collections import deque


class BinaryTree:
    def pre_order(self, root):
        if root is None:
            return
        print(root.val, end=" ")
        self.pre_order(root.left)
        self.pre_order(root.right)
        
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.val, end=" ")
        self.inorder(root.right)
    
    def post_order(self, root):
        if root is None:
            return
        self.inorder(root.left)
        self.inorder(root.right)
        print(root.val)
        
    def bfs(self, root):
        if root is None:
            return []
        queue = deque()
        queue.append(root)
        bfs = []
        while queue:
            level = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                level.append(curr.val)
            bfs.append(level)
        return bfs
        
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # Iterative method using Stack
        stack = []
        traversal = []
        current = root
        while current is not None or stack:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                traversal.append(current.val)
                current = current.right
        return traversal
