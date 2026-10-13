class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
    
        nums.sort(key = lambda x:x*x)

        res = 0

        i = 0
        j = len(nums)-1


        while i < j:
            res += nums[j]*nums[j]
            res -= nums[i]*nums[i]
            i += 1
            j -= 1
        
        if i == j: res += nums[j]*nums[j]
        return res