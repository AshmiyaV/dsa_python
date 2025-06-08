from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    res = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.res = max(self.res, left + right)
        return 1 + max(left, right)
    
def list_to_tree(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    q = deque([root])
    i = 1
    while i < len(lst):
        node = q.popleft()
        if i < len(lst) and lst[i] is not None:
            node.left = TreeNode(lst[i])
            q.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            q.append(node.right)
        i += 1
    return root

# Test case 1
root1 = list_to_tree([1, 2, 3, 4, 5])
print(Solution().diameterOfBinaryTree(root1))  # Output: 3

# Test case 2
root2 = list_to_tree([1, 2])
print(Solution().diameterOfBinaryTree(root2))  # Output: 1