class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        i = 0
        j = len(piles)-2

        piles.sort()
        sm = 0
        while i < j:
            sm += piles[j]
            j -= 2
            i += 1
        return sm
