import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 0, max(piles)
        k = r

        while l <= r:
            m = (l + r) // 2
            hoursTaken = 0

            for p in piles:
                hoursTaken += math.ceil(p / m)
            
            if hoursTaken <= h:
                k = min(k, m)
                r = m - 1
            
            else: l = m + 1

        return k

piles = [3,6,7,11]
h = 8
print(Solution().minEatingSpeed(piles, h))

piles2 = [30,11,23,4,20]
h2 = 5
print(Solution().minEatingSpeed(piles2, h2))

piles3 = [30,11,23,4,20]
h3 = 6
print(Solution().minEatingSpeed(piles3, h3))