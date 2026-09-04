class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        gre = [0]*len(nums)
        les = [0]*len(nums)

        for i,v in enumerate(nums):
            if i == 0: gre[i] = v
            else:gre[i] = max(gre[i-1],v)

        for i,v in enumerate(reversed(nums)):
            if i == 0:les[i] = v
            else:les[i] = min(les[i-1],v)

        les.reverse()

        
 

        for i in range(len(nums)):
            sc = gre[i] - les[i]
            if sc <= k: return i


        return -1
