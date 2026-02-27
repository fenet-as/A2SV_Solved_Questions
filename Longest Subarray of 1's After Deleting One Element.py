class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        

      
        i = 0
        ct0 = 0
        max_s = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                ct0 += 1

            while ct0 > 1:
                if nums[i] == 0:
                    ct0 -= 1
                i += 1
            max_s = max(max_s,j-i+1)

        return max_s-1
