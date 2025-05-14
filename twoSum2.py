class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            currentSum = numbers[l] + numbers[r]
            if currentSum > target:
                r -= 1
            elif currentSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []
    
numbers = [2,7,11,15]
target = 9
print(Solution().twoSum(numbers, target))

numbers2 = [2,3,4]
target2 = 6
print(Solution().twoSum(numbers2, target2))

numbers3 = [-1,0]
target3 = -1
print(Solution().twoSum(numbers3, target3))