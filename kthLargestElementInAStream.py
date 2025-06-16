import heapq


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# Test Case 1
print("Test Case 1:")
ops = ["KthLargest", "add", "add", "add", "add", "add"]
args = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

obj = None
for op, arg in zip(ops, args):
    if op == "KthLargest":
        obj = KthLargest(arg[0], arg[1])
        print(f"{op}{arg} -> None")
    else:
        result = obj.add(arg[0])
        print(f"{op}{arg} -> {result}")

# Test Case 2
print("\nTest Case 2:")
ops = ["KthLargest", "add", "add", "add", "add"]
args = [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]

obj = None
for op, arg in zip(ops, args):
    if op == "KthLargest":
        obj = KthLargest(arg[0], arg[1])
        print(f"{op}{arg} -> None")
    else:
        result = obj.add(arg[0])
        print(f"{op}{arg} -> {result}")