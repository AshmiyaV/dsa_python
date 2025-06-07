from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # Recursive DFS
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # BFS
        # level = 0
        # q = deque([root])

        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level += 1
        # return level

        # Iterative DFS

        res = 0
        stack = [(root, 1)]

        while stack:
            node, depth = stack.pop()
            # if node:
            res = max(res, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return res

def list_to_tree(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    q = deque([root])
    i = 1
    while q and i < len(lst):
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

# 🔍 Test Cases
root1 = list_to_tree([3, 9, 20, None, None, 15, 7])
print(Solution().maxDepth(root1))  # Output: 3

root2 = list_to_tree([1, None, 2])
print(Solution().maxDepth(root2))  # Output: 2