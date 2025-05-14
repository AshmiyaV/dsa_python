class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        sets = set(nums)
        longest = 0

        for i in sets:
            if (i - 1) not in sets:
                length = 1
                while (i + length) in sets:
                    length += 1
                longest = max(length, longest)
        return longest
    
nums = [100,4,200,1,3,2]
print(Solution().longestConsecutive(nums))

nums2 = [0,3,7,2,5,8,4,6,0,1]
print(Solution().longestConsecutive(nums2))