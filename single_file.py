class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        num = 0
        for e in nums:
            num = num ^ e
        return num 
