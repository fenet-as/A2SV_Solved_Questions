class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        _max = prices[-1]
        profit = 0

        for e in prices[::-1]:
            _max = max(_max,e)
            profit = max(profit, _max - e)

        return profit

