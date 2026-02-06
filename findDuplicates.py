class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        res = []

        for i,v in enumerate(nums):
            ind = abs(v)-1
            if nums[ind] < 0:
                res.append(ind+1)
            nums[ind] *= -1
        return res
    

