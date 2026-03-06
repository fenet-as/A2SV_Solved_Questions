class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hm = defaultdict(int)
        hm[0] = 1

        for i in range(1,len(nums)):
            nums[i] += nums[i-1]

        ct = 0
        for e in nums:
            if hm[e%k] >0 :
                ct += hm[e%k] 

            hm[e%k] += 1
        return ct
