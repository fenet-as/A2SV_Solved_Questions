class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        i = 0
        count = 0
        while i < len(nums)-2:

            j = i+1
            d = nums[j]-nums[i] 

            while j < len(nums) and nums[j]-nums[j-1] == d:
                j += 1
            l = j-i
            if l >= 3:
                count += (l-2)*(l-1)//2
            
            i = j-1

        return count 


            



