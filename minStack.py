class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minStack.append(min(val, self.minStack[-1]) if self.minStack else val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

min_stack = MinStack()

print("push -2")
min_stack.push(-2)

print("push 0")
min_stack.push(0)

print("push -3")
min_stack.push(-3)

print("getMin:", min_stack.getMin())  # Should print -3

print("pop")
min_stack.pop()

print("top:", min_stack.top())        # Should print 0

print("getMin:", min_stack.getMin())  # Should print -2