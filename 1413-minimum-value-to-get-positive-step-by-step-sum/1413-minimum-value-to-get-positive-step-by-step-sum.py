class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        for i in range(1,len(nums)):
            nums[i] += nums[i-1]

        _min = min(nums)

        if _min >= 0:
            return 1
        else:
            return -1*(_min) + 1