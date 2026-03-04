class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hm = {0:-1}

        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        
        for i,v in enumerate(nums):
            if v%k in hm and i - hm[v%k] >= 2:
                return True
            if v%k not in hm:
                hm[v%k] = i 
        return False
