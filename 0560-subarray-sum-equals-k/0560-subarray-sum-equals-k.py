class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = defaultdict(int)
        hm[0] += 1

        for i in range(1,len(nums)):
            nums[i] += nums[i-1]

        count = 0
        for e in nums:
            if hm[e - k] > 0:
                count += hm[e-k]
            hm[e] += 1
        return count