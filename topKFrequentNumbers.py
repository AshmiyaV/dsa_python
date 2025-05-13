class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}

        for i in nums:
            count[i] = 1 + count.get(i, 0)

        freq = [[] for i in range(len(nums) + 1)]

        for n, c in count.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                
        return
    
nums = [1,1,1,2,2,3]
k = 2
print(Solution().topKFrequent(nums, k))

nums2 = [1]
k2 = 1
print(Solution().topKFrequent(nums2, k2))