class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        res = []

        nums.sort()
        for i in range(len(nums)):
            
            if nums[i] == target:
                ind = i
                while ind < len(nums) and nums[ind] == target:
                    res.append(ind)
                    ind += 1
                return res
        return res
                    