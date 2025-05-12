class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
         hashset = set()
         for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
         return False
    
nums = [1, 2, 3, 3]

print(Solution().hasDuplicate(nums))

nums2 = [1, 2, 3, 4]

print(Solution().hasDuplicate(nums2))