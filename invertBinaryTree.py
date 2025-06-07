from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        from collections import deque
        res = []
        q = deque([self])
        while q:
            node = q.popleft()
            if node:
                res.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                res.append(None)
        while res and res[-1] is None:
            res.pop()
        return str(res)
    
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    
def list_to_tree(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    q = deque([root])
    i = 1
    while q and i < len(lst):
        node = q.popleft()
        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            q.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            q.append(node.right)
        i += 1
    return root

# Test cases
root = list_to_tree([4,2,7,1,3,6,9])
print(Solution().invertTree(root))

root2 = list_to_tree([2,1,3])
print(Solution().invertTree(root2))

root3 = list_to_tree([])
print(Solution().invertTree(root3))