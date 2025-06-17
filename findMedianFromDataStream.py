import heapq

class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        if self.small and self.large and -self.small[0] > self.large[0]:
            heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-self.small[0] + self.large[0]) / 2


# Simulate input
ops = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
args = [[], [1], [2], [], [3], []]

res = []
obj = None

for op, arg in zip(ops, args):
    if op == "MedianFinder":
        obj = MedianFinder()
        res.append(None)
    elif op == "addNum":
        obj.addNum(arg[0])
        res.append(None)
    elif op == "findMedian":
        res.append(obj.findMedian())

print(res)