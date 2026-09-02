class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cp = 0

        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:cp += prices[i] - prices[i-1]

        return cp