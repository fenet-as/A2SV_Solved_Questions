class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        

        j = len(nums)-1
        ct = 0
        mn = nums[-1]
        while j >= 0:
            if nums[j] > mn:
                k = ceil(nums[j]/ mn)
                mn = nums[j]//k
                ct += (k-1)
            else:
                mn = nums[j]
  
            j -= 1
        return ct

        
