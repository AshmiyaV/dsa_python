import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        res, minHeap = [], []

        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)

        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1

        return res
    
# Instantiate solution
sol = Solution()

# Test case 1
points1 = [[1,3],[-2,2]]
k1 = 1
output1 = sol.kClosest(points1, k1)
print(f"Input: points = {points1}, k = {k1}")
print(f"Output: {output1}\n")

# Test case 2
points2 = [[3,3],[5,-1],[-2,4]]
k2 = 2
output2 = sol.kClosest(points2, k2)
print(f"Input: points = {points2}, k = {k2}")
print(f"Output: {output2}")