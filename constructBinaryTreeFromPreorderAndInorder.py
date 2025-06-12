from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
    
def printLevelOrder(root: Optional[TreeNode]):
    if not root:
        print("Level-order output: []")
        return

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()

    print("Level-order output:", result)

# Run both examples
def run_example(preorder, inorder):
    print("\n==== NEW EXAMPLE ====")
    print(f"Input preorder: {preorder}")
    print(f"Input inorder:  {inorder}")
    solution = Solution()
    root = solution.buildTree(preorder, inorder)
    printLevelOrder(root)

# Example 1
run_example([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])

# Example 2
run_example([-1], [-1])