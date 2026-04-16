class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        missing = ( (n*(n+1))//2) - sum(nums)
        

       
        for i in range(n):
            ind = abs(nums[i])-1

            if nums[ind] < 0:
                return [ind + 1,missing+ind+1]

            nums[ind] *= -1

        


