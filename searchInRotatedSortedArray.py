class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            elif nums[m] >= nums[l]:
                if target > m or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1

            else:
                if target < m or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
            
        return -1

nums = [4,5,6,7,0,1,2]
target = 0
print(Solution().search(nums, target))

nums2 = [4,5,6,7,0,1,2]
target2 = 3
print(Solution().search(nums2, target2))

nums3 = [1]
target3 = 0
print(Solution().search(nums3, target3))