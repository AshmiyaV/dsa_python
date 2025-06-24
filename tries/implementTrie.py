class TreeNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TreeNode()
            curr = curr.children[c]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.isEnd            

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

ops = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
args = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

trie = None
output = []

for op, arg in zip(ops, args):
    if op == "Trie":
        trie = Trie()
        output.append(None)
    elif op == "insert":
        trie.insert(arg[0])
        output.append(None)
    elif op == "search":
        output.append(trie.search(arg[0]))
    elif op == "startsWith":
        output.append(trie.startsWith(arg[0]))

print(output)