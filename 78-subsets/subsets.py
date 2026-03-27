class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def explore(i):
            if i == len(nums):
                res.append(path[:])
                return
            res.append(path[:])
            for j in range(i,len(nums)):
                path.append(nums[j])
                explore(j+1)
                path.pop()
            return 

        explore(0)
        return res