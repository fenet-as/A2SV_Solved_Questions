class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        re = len(nums)-1
        le = 0

        r = 0
        while r <= re:

            if nums[r] == 0:
                nums[le],nums[r] = nums[r],nums[le]
                le += 1
                r += 1

            elif nums[r] == 2:
                nums[re],nums[r] = nums[r],nums[re]
                re -= 1
            else:
                r += 1

            
        
 