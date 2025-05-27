class Solution:
    def findMin(self, nums: list[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])

            if nums[m] > nums[l]:
                l = l + 1

            else:
                r = r - 1

        return res

nums = [3,4,5,1,2]
print(Solution().findMin(nums))

nums2 = [4,5,6,7,0,1,2]
print(Solution().findMin(nums2))

nums3 = [11,13,15,17]
print(Solution().findMin(nums3))