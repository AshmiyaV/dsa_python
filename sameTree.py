from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 
    
sol = Solution()

# Example 1: p = [1,2,3], q = [1,2,3]
p1 = TreeNode(1, TreeNode(2), TreeNode(3))
q1 = TreeNode(1, TreeNode(2), TreeNode(3))
print("Example 1:", sol.isSameTree(p1, q1))  # Output: True

# Example 2: p = [1,2], q = [1,null,2]
p2 = TreeNode(1, TreeNode(2))
q2 = TreeNode(1, None, TreeNode(2))
print("Example 2:", sol.isSameTree(p2, q2))  # Output: False
        