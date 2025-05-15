class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                currentSum = n + nums[l] + nums[r]
                if currentSum > 0:
                    r -= 1
                elif currentSum < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res
    
nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))

nums2 = [0,1,1]
print(Solution().threeSum(nums2))

nums3 = [0,0,0]
print(Solution().threeSum(nums3))