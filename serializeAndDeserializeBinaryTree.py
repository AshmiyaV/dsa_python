class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right) 
        dfs(root)
        return (",").join(res)

    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0
        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()      

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

from collections import deque
def print_tree_level_order(root):
    if not root:
        print([])
        return
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    print(result)

# Example 1: [1,2,3,null,null,4,5]
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

ser = Codec()
deser = Codec()
data = ser.serialize(n1)
print("Serialized:", data)

tree = deser.deserialize(data)
print("Deserialized tree level order:")
print_tree_level_order(tree)

# Example 2: empty tree
empty_data = ser.serialize(None)
print("\nSerialized empty tree:", empty_data)
empty_tree = deser.deserialize(empty_data)
print("Deserialized empty tree:")
print_tree_level_order(empty_tree)