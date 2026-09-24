class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        

        for i,v in enumerate(nums):
            sm = 0
            cn = v
            while cn > 0:
                sm += cn % 10
                cn //= 10
            if sm == i: return i
        return -1

            