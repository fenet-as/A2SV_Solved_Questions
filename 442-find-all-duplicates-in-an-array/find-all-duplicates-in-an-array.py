class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []


        for e in nums:
            c_ind = abs(e)-1
            

            if nums[c_ind] < 0:
                res.append(c_ind+1)
            else:
                nums[c_ind] *= -1
        return res
