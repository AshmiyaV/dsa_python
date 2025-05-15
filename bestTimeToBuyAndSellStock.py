class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxRes = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxRes = max(maxRes, profit)
            else:
                l = r
            r += 1

        return maxRes
    
prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))

prices2 = [7,6,4,3,1]
print(Solution().maxProfit(prices2))