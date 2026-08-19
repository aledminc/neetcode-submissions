class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        for i in range(len(prices) - 1):
            for j in prices[i+1:]:
                if j - prices[i] > maxp:
                    maxp = j - prices[i]
        return maxp

            