class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        path = []
        def helper(i):
            if i >= len(nums):
                res.append(path[:])
                return 

            # if path not in res:
            #     res.append(path[:])

            for j in range(i,len(nums)):
                if path not in res:
                    res.append(path[:])
                path.append(nums[j])
                helper(j+1)
                path.pop()

            return 
        helper(0)
        return res