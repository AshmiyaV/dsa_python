from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        res = []
        q = deque([root])

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res
    
sol = Solution()

# Example 1: root = [3,9,20,null,null,15,7]
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20, TreeNode(15), TreeNode(7))
print("Example 1:", sol.levelOrder(root1))  # Output: [[3],[9,20],[15,7]]

# Example 2: root = [1]
root2 = TreeNode(1)
print("Example 2:", sol.levelOrder(root2))  # Output: [[1]]

# Example 3: root = []
root3 = None
print("Example 3:", sol.levelOrder(root3))  # Output: []