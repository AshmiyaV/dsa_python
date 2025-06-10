from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val 
            curr = curr.right

def insertLevelOrder(arr, i):
    if i < len(arr) and arr[i] is not None:
        root = TreeNode(arr[i])
        root.left = insertLevelOrder(arr, 2 * i + 1)
        root.right = insertLevelOrder(arr, 2 * i + 2)
        return root
    return None

# Tree input and execution
arr1 =  [3,1,4,None,2]
k1 = 1
root1 = insertLevelOrder(arr1, 0)

arr2 = [5,3,6,2,4,None,None,1]
k2 = 3
root2 = insertLevelOrder(arr2, 0)

sol = Solution()
result1 = sol.kthSmallest(root1, k1)
result = sol.kthSmallest(root1, k2)
print("Result:", result1)
print("Result:", result)