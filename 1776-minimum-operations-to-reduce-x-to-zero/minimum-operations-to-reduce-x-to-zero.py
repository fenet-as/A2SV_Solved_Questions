class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        

     
        mn = float("inf")
        t = sum(nums) - x

        i = 0
        cs = 0 

        for j in range(len(nums)):
            cs += nums[j]
           
            while i <= j and cs > t: 
                cs -= nums[i]
                i += 1

            if cs == t: mn = min(mn,len(nums)- ((j-i)+1))

         

        if mn == float("inf"):return -1
        return mn

            

            
