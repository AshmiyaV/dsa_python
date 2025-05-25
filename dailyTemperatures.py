class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        tempStack = []

        for i, t in enumerate(temperatures):
            while tempStack and t > tempStack[-1][1]:
                index, temp = tempStack.pop()
                res[index] = i - index
            
            tempStack.append([i, t])

        return res

temperatures = [73,74,75,71,69,72,76,73]
print(Solution().dailyTemperatures(temperatures))

temperatures2 = [30,40,50,60]
print(Solution().dailyTemperatures(temperatures2))

temperatures3 = [30,60,90]
print(Solution().dailyTemperatures(temperatures3))