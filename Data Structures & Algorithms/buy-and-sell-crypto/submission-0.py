class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        profit = 0
        initialElement = prices[0]
        n = len(prices)
        for i in range(n):
            if prices[i] < initialElement:
                initialElement = prices[i]
            else:
                profit = prices[i] - initialElement
                maxProfit = max(maxProfit, profit)
        return maxProfit