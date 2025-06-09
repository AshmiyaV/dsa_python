class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr
            
# Build example tree: [6,2,8,0,4,7,9,null,null,3,5]
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

sol = Solution()

# Example 1: p = 2, q = 8
p1 = root.left         # Node 2
q1 = root.right        # Node 8
print("Example 1:", sol.lowestCommonAncestor(root, p1, q1).val)  # Output: 6

# Example 2: p = 2, q = 4
p2 = root.left         # Node 2
q2 = root.left.right   # Node 4
print("Example 2:", sol.lowestCommonAncestor(root, p2, q2).val)  # Output: 2

# Example 3: root = [2,1], p = 2, q = 1
root2 = TreeNode(2)
root2.left = TreeNode(1)
p3 = root2             # Node 2
q3 = root2.left        # Node 1
print("Example 3:", sol.lowestCommonAncestor(root2, p3, q3).val)  # Output: 2
        