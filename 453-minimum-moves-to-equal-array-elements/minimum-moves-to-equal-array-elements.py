class Solution:
    def minMoves(self, nums: list[int]) -> int:
        

        count = 0
        mn = min(nums)

        for e in nums:
            count += e - mn
        
        return count


