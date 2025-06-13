from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Helper function to build tree from level-order input
def build_tree(level_order: List[Optional[int]]) -> Optional[TreeNode]:
    if not level_order or level_order[0] is None:
        return None
    root = TreeNode(level_order[0])
    queue = deque([root])
    i = 1
    while queue and i < len(level_order):
        node = queue.popleft()
        if level_order[i] is not None:
            node.left = TreeNode(level_order[i])
            queue.append(node.left)
        i += 1
        if i < len(level_order) and level_order[i] is not None:
            node.right = TreeNode(level_order[i])
            queue.append(node.right)
        i += 1
    return root

# Solution class
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)
            res = max(res, node.val + leftMax + rightMax)
            return node.val + max(leftMax, rightMax)

        dfs(root)
        return res

# Example test cases
sol = Solution()
tree1 = build_tree([-10, 9, 20, None, None, 15, 7])
tree2 = build_tree([1, 2, 3])

print("Max path sum for [-10,9,20,null,null,15,7]:", sol.maxPathSum(tree1))  # Output should be 42
print("Max path sum for [1,2,3]:", sol.maxPathSum(tree2))  # Output should be 6
