class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        i = 0
        while i < len(nums):

            while 1 <= nums[i] <= len(nums) and nums[i]-1 != i and nums[nums[i] - 1] != nums[i]:
                vind = nums[i]-1
                nums[i],nums[vind] = nums[vind] , nums[i]
                
            i += 1


        # print(nums) 
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1


        return len(nums)+1