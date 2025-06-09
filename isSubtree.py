from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSame(self, p, q):
        if not p and not q:
            return True
        if not p or not q or (p.val != q.val):
            return False
        return self.isSame(p.left, q.left) and self.isSame(p.right, q.right)
    
sol = Solution()

# Example 1
# root = [3,4,5,1,2]
root1 = TreeNode(3)
root1.left = TreeNode(4, TreeNode(1), TreeNode(2))
root1.right = TreeNode(5)

# subRoot = [4,1,2]
subRoot1 = TreeNode(4, TreeNode(1), TreeNode(2))

print("Example 1:", sol.isSubtree(root1, subRoot1))  # Output: True

# Example 2
# root = [3,4,5,1,2,null,null,null,null,0]
root2 = TreeNode(3)
root2.left = TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0)))
root2.right = TreeNode(5)

# subRoot = [4,1,2]
subRoot2 = TreeNode(4, TreeNode(1), TreeNode(2))

print("Example 2:", sol.isSubtree(root2, subRoot2))  # Output: False
