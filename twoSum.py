class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i

nums = [2,7,11,15]
target = 9
print(Solution().twoSum(nums, target))

nums2 = [3,2,4]
target2 = 6
print(Solution().twoSum(nums2, target2))