from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        q = deque([root])

        while q:
            rightNode = None
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    rightNode = node.val
                    q.append(node.left)
                    q.append(node.right)
            if rightNode is not None:
                res.append(rightNode)

        return res
    

sol = Solution()

# Example 1: root = [1,2,3,null,5,null,4]
root1 = TreeNode(1)
root1.left = TreeNode(2, None, TreeNode(5))
root1.right = TreeNode(3, None, TreeNode(4))
print("Example 1:", sol.rightSideView(root1))  # Output: [1, 3, 4]

# Example 2: root = [1,2,3,4,null,null,null,5]
root2 = TreeNode(1)
root2.left = TreeNode(2, TreeNode(4, TreeNode(5)))
root2.right = TreeNode(3)
print("Example 2:", sol.rightSideView(root2))  # Output: [1, 3, 4, 5]

# Example 3: root = [1, null, 3]
root3 = TreeNode(1, None, TreeNode(3))
print("Example 3:", sol.rightSideView(root3))  # Output: [1, 3]

# Example 4: root = []
root4 = None
print("Example 4:", sol.rightSideView(root4))  # Output: []