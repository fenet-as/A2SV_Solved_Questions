class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        hm = defaultdict(int)
        hm[0] += 1

        for i in range(1,len(nums)):
            nums[i] += nums[i-1]

        ct = 0

        for e in nums:
            if hm[e - goal] > 0:
                ct += hm[e-goal]
            
            hm[e] += 1
        return ct
