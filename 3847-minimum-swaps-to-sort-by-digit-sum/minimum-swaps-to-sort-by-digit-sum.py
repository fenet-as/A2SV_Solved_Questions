class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        def summ(n):
            sm = 0

            while n > 0:
                sm += n % 10
                n //= 10
            return sm
             
        for i in range(len(nums)):
            nums[i] = (nums[i],i)



        nums.sort(key = lambda x:[summ(x[0]),x[0]])
        


        seen = set()

        sm = 0
        for i in range(len(nums)):
            s = i
            ct = 0
            while s not in seen:
                ct += 1
                seen.add(s)
                s = nums[s][1]
            sm += max(0,ct - 1)
        return sm 
            
            






            

                    
