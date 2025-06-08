from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]

    def dfs(self, root):
        if not root:
            return (True, 0)
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        balanced = left[0] and right[0] and (abs(left[1] - right[1]) <= 1)

        return (balanced, 1 + max(left[1], right[1]))

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
    
root1 = list_to_tree([3, 9, 20, None, None, 15, 7])
print(Solution().isBalanced(root1))  # Expected: True

root2 = list_to_tree([1, 2, 2, 3, 3, None, None, 4, 4])
print(Solution().isBalanced(root2))  # Expected: False

        