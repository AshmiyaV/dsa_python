class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    
        def dfs(node, maxVal):
            if not node:
                return 0
            res = 1 if node.val >= maxVal else 0

            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            return res

        return dfs(root, root.val)
    
sol = Solution()

# Example 1: root = [3,1,4,null,null,1,5]
root1 = TreeNode(3)
root1.left = TreeNode(1)
root1.left.left = TreeNode(3)
root1.right = TreeNode(4)
root1.right.left = TreeNode(1)
root1.right.right = TreeNode(5)
print("Example 3:", sol.goodNodes(root1)) 

# Example 2: root = [3,3,null,4,2]
root2 = TreeNode(3)
root2.left = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(2)
print("Example 2:", sol.goodNodes(root2))  # Output: 3

# Example 3: root = [1]
root3 = TreeNode(1)
print("Example 3:", sol.goodNodes(root3))  # Output: 1