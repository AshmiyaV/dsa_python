class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result
    
nums = [1,2,3,4]
print(Solution().productExceptSelf(nums))

nums2 = [-1,1,0,-3,3]
print(Solution().productExceptSelf(nums2))