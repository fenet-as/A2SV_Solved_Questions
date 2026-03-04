class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]

        mn = 0
        mx = max(nums)

        for  e in nums:
            mx = max(e - mn,mx)
            mn = min(e,mn)
            
            
            
        return mx