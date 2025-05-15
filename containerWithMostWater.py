class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxArea = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            maxArea = max(maxArea, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea
    
height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))

height1 = [1,1]
print(Solution().maxArea(height1))