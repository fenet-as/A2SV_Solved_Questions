class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        n = len(nums)
        i = n-3
        j = n-2
        k = n-1

        while i >= 0:
            if (nums[j] + nums[k] > nums[i]) and (nums[j] + nums[i] > nums[k]) and (nums[i] + nums[k] > nums[j]):
                return nums[j] + nums[k] + nums[i]
            i -= 1
            j -= 1
            k -= 1

        return 0