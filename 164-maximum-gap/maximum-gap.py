class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        nums.sort()
        mx = 0
        for i in range(1,len(nums)):
            mx = max(nums[i]-nums[i-1],mx)

        return mx