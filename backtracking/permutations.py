class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 0:
            return [[]]

        res = []
        perms = self.permute(nums[1:])

        for p in perms:
            for i in range(0, len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)

        return res

nums = [1,2,3]
print(Solution().permute(nums))

nums2 = [0,1]
print(Solution().permute(nums2))

nums3 = [1]
print(Solution().permute(nums3))